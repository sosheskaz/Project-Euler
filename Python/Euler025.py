#!/usr/bin/env python3
import itertools
from numba import jit


@jit(nopython=True)
def main():
    fibs = fibonacci()

    # Calculating this once is faster than calling log10 over and over.
    target = 10 ** 999
    last_fib = next(itertools.dropwhile(lambda f: f[1] <= target, enumerate(fibs)))

    # enumerate() is zero-indexed. Fibonacci is not.
    index = last_fib[0] + 1

    print(index)


@jit(nopython=True)
def fibonacci():
    r1 = 1
    yield r1
    r2 = 1
    yield r2
    while True:
        cur = r1 + r2
        yield cur
        r1 = r2
        r2 = cur


main()
