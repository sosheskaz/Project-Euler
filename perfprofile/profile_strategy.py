import json
import os
from time import time, sleep
import stat
from subprocess import check_call, check_output, call, Popen, DEVNULL
import shutil
import traceback
import docker


class ProfileStrategy(object):
    '''A strategy for profiling the performance of PE problems.'''
    name = 'PROFILE'
    extensions = {}
    iterations = 10
    docker_image = None

    docker_volumes = {
        os.path.realpath(os.path.join(os.path.dirname(__file__), '..')): {
            'bind': '/workspace',
            'mode': 'rw'
        }
    }
    docker_entrypoint = ['tail', '-f', '/dev/null']

    @property
    def docker_run_args(self):
        return {
            'volumes': self.docker_volumes,
            'working_dir': '/workspace',
            'detach': True,
            'entrypoint': self.docker_entrypoint,
            'remove': True,
            'user': os.getuid()
        }

    docker_exec_args = {
        'stdout': True,
        'stderr': True
    }

    _docker_client = None
    _docker_container = None

    def __init__(self):
        self._docker_client = docker.from_env()

    def matches_file(self, f):
        return os.path.splitext(f)[1] in self.extensions

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, tb):
        self.close()

    def open(self):
        if self.docker_image:
            try:
                self._docker_client.images.get(self.docker_image)
            except docker.errors.ImageNotFound:
                self._docker_client.images.pull(self.docker_image)
            self._docker_container = self._docker_client.containers.run(self.docker_image, **self.docker_run_args)

    def command_for(self, f):
        raise NotImplementedError()

    def close(self):
        '''Closes used resources like docker'''
        if self._docker_container:
            self._docker_container.kill()
        self._docker_client.close()

    def setup_for(self, f):
        '''Does any needed setup, like compilation.'''
        pass

    def cleanup_for(self, f):
        '''Cleans up any artifacts created by setup or execution.'''
        pass

    def exec(self, command):
        if self._docker_container:
            return self._docker_container.exec_run(command, **self.docker_exec_args)
        else:
            p = Popen(command, stdout=DEVNULL, stderr=DEVNULL)
            stdout, _ = p.communicate()
            rc = p.returncode
            return (rc, stdout)

    def time_file(self, f):
        '''Runs the file.'''
        command = ['perfprofile/profile.bin', *self.command_for(f)]
        _, output = self.exec(command)
        try:
            result = json.loads(output)
        except json.JSONDecodeError as jde:
            print('Command failed: {}'.format(command))
            print('Failed to decode output JSON:')
            print(output)
            traceback.print_exc()
            raise jde
        return result

    def get_perf_profile(self, f):
        '''invokes run_file inside time to get perf data.'''
        self.setup_for(f)
        result = self.time_file(f)
        self.cleanup_for(f)
        return result


class ShebangError(Exception):
    pass


class ShebangStrategy(ProfileStrategy):
    name = 'Shebang'
    extensions = {'.groovy', '.js', '.py', '.rb'}
    docker_image = 'groovy:2.5.6-jdk8'

    def _has_shebang(self, f):
        with open(f) as fd:
            return fd.read(2) == '#!'

    def matches_file(self, f):
        return super().matches_file(f) and self._has_shebang(f)

    def setup_for(self, f):
        if not self._has_shebang(f):
            raise ShebangError('{} does not have a shebang.'.format(f))

        # Make the file executable if it's not already.
        if not os.access(f, os.X_OK):
            st = os.stat(f)
            # chmod +x
            os.chmod(f, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    def command_for(self, f):
        return [f]


class GroovyDirectStrategy(ShebangStrategy):
    name = 'Groovy 2.5.6/JDK8 (Standard)'
    extensions = {'.groovy', '.gvy', '.gy', '.gsh'}
    iterations = 3


class GroovyNailgunStrategy(ProfileStrategy):
    name = 'Groovy 2.5.6/JDK8 (NailGun)'
    extensions = {'.groovy', '.gvy', '.gy', '.gsh'}
    docker_image = 'ericmiller/groovy-nailgun:2.5.6-jdk8'
    docker_entrypoint = None

    _ng_proc = None

    def command_for(self, f):
        return ['ng-groovy', f]

    def setup_for(self, f):
        # Do the first execution to make sure classpath is all loaded up
        retries = 10
        delay = 0.1
        while self.exec(self.command_for(f)) != 0 and retries > 0:
            sleep(delay)  # I know, I know.
            retries -= 1


class Node12Strategy(ShebangStrategy):
    name = 'Node.js 12.3.0'
    extensions = {'.js'}
    docker_image = 'node:12.3.0-alpine'


class Node11Strategy(Node12Strategy):
    name = 'Node.js 11.15.0'
    docker_image = 'node:11.15.0-alpine'


class Node10Strategy(Node12Strategy):
    name = 'Node.js 10.15.3'
    docker_image = 'node:10.15.3-alpine'


class CPython3Strategy(ShebangStrategy):
    name = 'CPython 3.7.3'
    extensions = {'.py'}
    docker_image = 'python:3.7.3-alpine'


class CPython2Strategy(CPython3Strategy):
    name = 'CPython 2.7.16'
    docker_image = 'python:2.7.16-alpine'

    def command_for(self, f):
        return ['python2', f]


class PyPy3Strategy(ShebangStrategy):
    name = 'PyPy 3.6-7.1.1'
    extensions = {'.py'}
    docker_image = 'pypy:3.6-7.1.1-slim'

    def command_for(self, f):
        return ['pypy3', f]


class PyPy2Strategy(PyPy3Strategy):
    name = 'PyPy 2.7-7.1.1'
    docker_image = 'pypy:2.7-7.1.1-slim'

    def command_for(self, f):
        return ['pypy', f]


class RubyStrategy(ShebangStrategy):
    name = 'Ruby 2.6.0'
    extensions = {'.rb'}
    docker_image = 'ruby:2.6.0-alpine'


class GoStrategy(ProfileStrategy):
    name = 'Go 1.12'
    golibs = ['Go/sieve.go', 'Go/combinatorics.go']
    docker_image = 'golang:1.12'

    @property
    def docker_volumes(self):
        volumes = super().docker_volumes
        additional = {
            '/tmp/project-euler/.cache': {
                'bind': '/.cache',
                'mode': 'rw'
            }
        }
        volumes.update(additional)
        return volumes

    extensions = {'.go'}
    # Since go is compiled, it is much much faster, so we use more iterations.
    iterations = 20

    def _target_for(self, f):
        return '{}.bin'.format(f)

    def command_for(self, f):
        return [self._target_for(f)]

    def setup_for(self, f):
        target = self._target_for(f)
        self.exec(['go', 'build', '-o', target, f, *self.golibs])

    def cleanup_for(self, f):
        target = self._target_for(f)
        if os.path.isfile(target):
            os.remove(target)


class CSharpStrategy(ProfileStrategy):
    name = 'C#'
    extensions = {'.csproj'}

    @property
    def docker_volumes(self):
        volumes = super().docker_volumes
        additional = {
            '/tmp/project-euler/.dotnet': {
                'bind': '/.dotnet',
                'mode': 'rw'
            },
            '/tmp/project-euler/.nuget': {
                'bind': '/.nuget',
                'mode': 'rw'
            }
        }
        volumes.update(additional)
        return volumes


class CSharpDotNetCoreStrategy(CSharpStrategy):
    _version = '2.2'

    @property
    def name(self):
        return 'C# .NET Core {}'.format(self._version)

    @property
    def docker_image(self):
        return 'mcr.microsoft.com/dotnet/core/sdk:{}'.format(self._version)

    def setup_for(self, f):
        self.exec(['dotnet', 'build', '-o', 'bin', f])

    def command_for(self, f):
        dll_file = '{}.dll'.format(os.path.splitext(os.path.basename(f))[0])
        dll_file = os.path.join(os.path.dirname(f), 'bin', dll_file)

        return ['dotnet', dll_file]

    def cleanup_for(self, f):
        shutil.rmtree(os.path.join(os.path.dirname(f), 'bin'))


class KotlinStrategy(ProfileStrategy):
    name = 'Kotlin 1.3/JDK 12'
    extensions = {'.kt'}
    docker_image = 'zenika/kotlin:1.3-jdk12-alpine'
    ktlibs = ['Kotlin/Sieve.kt', 'Kotlin/Combinatorics.kt']

    def _target_for(self, f):
        return '{}.jar'.format(f)

    def command_for(self, f):
        return ['java', '-jar', self._target_for(f)]

    def setup_for(self, f):
        super().setup_for(f)
        self.exec(['kotlinc', f, *self.ktlibs, '-include-runtime', '-d', self._target_for(f)])

    def cleanup_for(self, f):
        super().cleanup_for(f)
        target = self._target_for(f)
        if os.path.isfile(target):
            os.remove(target)


STRATEGIES = [
    Node12Strategy,
    Node11Strategy,
    Node10Strategy,
    CPython3Strategy,
    CPython2Strategy,
    RubyStrategy,
    GroovyDirectStrategy,
    GroovyNailgunStrategy,
    GoStrategy,
    CSharpDotNetCoreStrategy,
    KotlinStrategy
]

def strategies_for(f):
    return (strat for strat in STRATEGIES if strat.matches_file(f))
