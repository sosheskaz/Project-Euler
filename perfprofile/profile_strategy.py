import os
from time import time
import stat
from subprocess import check_call, DEVNULL


class ProfileStrategy(object):
    '''A strategy for profiling the performance of PE problems.'''
    name = 'PROFILE'
    extensions = {}
    iterations = 10

    def matches_file(self, f):
        return os.path.splitext(f)[1] in self.extensions

    def setup_for(self, f):
        '''Does any needed setup, like compilation.'''
        pass

    def cleanup_for(self, f):
        '''Cleans up any artifacts created by setup or execution.'''
        pass

    def run_file(self, f):
        '''Runs the file.'''
        raise NotImplementedError()

    def get_perf_profile(self, f):
        '''invokes run_file inside time to get perf data.'''
        self.setup_for(f)
        start = time()
        for _ in range(0, self.iterations):
            self.run_file(f)
        end = time()
        self.cleanup_for(f)
        return (end - start) / self.iterations


class ShebangError(Exception):
    pass


class ShebangStrategy(ProfileStrategy):
    name = 'Shebang'
    extensions = {'.groovy', '.js', '.py', '.rb'}

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

    def run_file(self, f):
        check_call(os.path.realpath(f), stdout=DEVNULL, stderr=DEVNULL)


class LazyGroovyStrategy(ShebangStrategy):
    name = 'Groovy'
    extensions = {'.groovy', '.gvy', '.gy', '.gsh'}
    # Groovy's massive startup time (to spin up JVM) means that values are
    # already stable
    iterations = 3


class LazyJavaScriptStrategy(ShebangStrategy):
    name = 'JavaScript'
    extensions = {'.js'}


class LazyPythonStrategy(ShebangStrategy):
    name = 'Python'
    extensions = {'.py'}


class LazyRubyStrategy(ShebangStrategy):
    name = 'Ruby'
    extensions = {'.rb'}


class CompiledGoStrategy(ProfileStrategy):
    name = 'Go (Compiled)'
    extensions = {'.go'}
    # Since go is compiled, it is much much faster, so we use more iterations.
    iterations = 20

    def _target_for(self, f):
        return '{}.bin'.format(f)

    def setup_for(self, f):
        target = self._target_for(f)
        check_call(['go', 'build', '-o', target, f])

    def run_file(self, f):
        target = os.path.realpath(self._target_for(f))
        check_call([target], stdout=DEVNULL, stderr=DEVNULL)

    def cleanup_for(self, f):
        target = self._target_for(f)
        if os.path.isfile(target):
            os.remove(target)

STRATEGIES = [
    LazyGroovyStrategy(),
    LazyJavaScriptStrategy(),
    LazyPythonStrategy(),
    LazyRubyStrategy(),
    CompiledGoStrategy()
]

def strategies_for(f):
    return (strat for strat in STRATEGIES if strat.matches_file(f))
