#!/usr/bin/env python3
from __future__ import print_function
import os
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    target = 1000000

    chains = (collatz(i) for i in range(1, target))

    biggest = max(chains, key=lambda chain: len(chain))

    print(biggest[0])


def collatz(n):
    result = []

    while n > 1:
        result.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    result.append(n)
    return result


if __name__ == '__main__':
    main()
