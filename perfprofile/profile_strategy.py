import json
import os
from time import time, sleep
import stat
from subprocess import check_call, check_output, call, Popen, DEVNULL
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
        result = json.loads(output)
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


class LazyJavaScriptStrategy(ShebangStrategy):
    name = 'Node.js 12.3.0'
    extensions = {'.js'}
    docker_image = 'node:12.3.0-alpine'


class LazyPythonStrategy(ShebangStrategy):
    name = 'Python 3.7.3'
    extensions = {'.py'}
    docker_image = 'python:3.7.3-alpine'


class PyPyStrategy(ShebangStrategy):
    name = 'PyPy 3.6-7.1.0'
    extensions = {'.py'}
    docker_image = 'pypy:3.6-7.1.0-slim'

    def command_for(self, f):
        return ['pypy3', f]


class JythonStrategy(ShebangStrategy):
    name = 'Jython 2.7 (Nailgun)'
    extensions = {'.py'}
    docker_image = 'ericmiller/jython-nailgun:2.7'

    def command_for(self, f):
        return ['ng-jython', f]


class LazyRubyStrategy(ShebangStrategy):
    name = 'Ruby 2.6.0'
    extensions = {'.rb'}
    docker_image = 'ruby:2.6.0-alpine'


class JrubyStrategy(ShebangStrategy):
    name = 'JRuby 9.2 (Nailgun)'
    extensions = {'.rb'}
    docker_image = 'ericmiller/jruby-nailgun:9.2'

    def command_for(self, f):
        return ['ng-jruby', f]


class GoStrategy(ProfileStrategy):
    name = 'Go 1.12.3'
    golibs = ['Go/sieve.go']
    docker_image = 'golang:1.12'


class GoRunStrategy(GoStrategy):
    @property
    def name(self):
        return '{} (Run)'.format(super().name)
    extensions = {'.go'}
    iterations = 3

    def command_for(self, f):
        return ['go', 'run', f, *self.golibs]


class CompiledGoStrategy(GoStrategy):
    @property
    def name(self):
        return '{} (Compiled)'.format(super().name)

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

STRATEGIES = [
    LazyJavaScriptStrategy,
    LazyPythonStrategy,
    LazyRubyStrategy,
    GroovyDirectStrategy,
    GroovyNailgunStrategy,
    GoRunStrategy,
    CompiledGoStrategy
]

def strategies_for(f):
    return (strat for strat in STRATEGIES if strat.matches_file(f))
