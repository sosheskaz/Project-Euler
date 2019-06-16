#!/usr/bin/env python3
from __future__ import print_function
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    s = sum(range(3, 1000, 3)) + sum(i for i in range(5, 1000, 5) if i % 3)
    print(s)


if __name__ == '__main__':
    main()
