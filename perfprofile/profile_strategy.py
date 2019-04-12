import os
from time import time, sleep
import stat
from subprocess import check_call, call, Popen, DEVNULL
import docker


class ProfileStrategy(object):
    '''A strategy for profiling the performance of PE problems.'''
    name = 'PROFILE'
    extensions = {}
    iterations = 10
    docker_image = None

    docker_volumes = {
        os.path.realpath(os.curdir): {
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
        'stdout': False,
        'stderr': False
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
            check_call(command, stdout=DEVNULL, stderr=DEVNULL)

    def time_file(self, f):
        '''Runs the file.'''
        command = self.command_for(f)
        if self._docker_container:
            start = time()
            self.exec(command)
            end = time()
        else:
            start = time()
            check_call(command, stdout=DEVNULL, stderr=DEVNULL)
            end = time()
        return end - start

    def get_perf_profile(self, f):
        '''invokes run_file inside time to get perf data.'''
        self.setup_for(f)
        _time = sum(self.time_file(f) for _ in range(0, self.iterations)) / self.iterations
        self.cleanup_for(f)
        return _time


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
    name = 'Groovy (Direct)'
    extensions = {'.groovy', '.gvy', '.gy', '.gsh'}
    iterations = 3


class GroovyNailgunStrategy(ProfileStrategy):
    name = 'Groovy (NailGun)'
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
    name = 'JavaScript'
    extensions = {'.js'}
    docker_image = 'node:8.15.1-alpine'


class LazyPythonStrategy(ShebangStrategy):
    name = 'Python'
    extensions = {'.py'}
    docker_iamge = 'python:3.7.3-alpine'


class LazyRubyStrategy(ShebangStrategy):
    name = 'Ruby'
    extensions = {'.rb'}
    docker_image = 'ruby:2.6.0-alpine'


class GoStrategy(ProfileStrategy):
    golibs = ['Go/sieve.go']
    docker_image = 'golang:1.12-alpine'


class GoRunStrategy(GoStrategy):
    name = 'Go (Go Run)'
    extensions = {'.go'}
    iterations = 3

    def command_for(self, f):
        return ['go', 'run', f, *self.golibs]


class CompiledGoStrategy(GoStrategy):
    name = 'Go (Compiled)'
    extensions = {'.go'}
    # Since go is compiled, it is much much faster, so we use more iterations.
    iterations = 20

    def _target_for(self, f):
        return '{}.bin'.format(f)

    def command_for(self, f):
        return [os.path.realpath(self._target_for(f))]

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
