#!/usr/bin/env python3
from __future__ import print_function, division
from itertools import permutations, islice
import itertools
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    target = 1000000
    digits = list(range(0, 10))
    perms = permutations(digits)
    result = next(islice(perms, target - 1, target))
    result = ''.join(str(d) for d in result)
    print(result)


if __name__ == '__main__':
    main()
