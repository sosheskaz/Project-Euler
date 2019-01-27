#!/usr/bin/env python
from __future__ import print_function
from itertools import takewhile


def main():
    fibs = fibonacci()
    evens = (fib for fib in fibs if not fib % 2)
    under_4m = takewhile(lambda x: x < 4000000, evens)
    print(sum(under_4m))


def fibonacci():
    previous = 1
    current = 1
    yield previous
    yield current

    while True:
        old_prev = previous
        previous = current
        current = previous + old_prev
        yield current


if __name__ == '__main__':
    main()
