#!/usr/bin/env python
from __future__ import print_function


def main():
    s = sum(range(3, 1000, 3))

    s += sum(i for i in range(5, 1000, 5) if i % 3)

    print(s)


if __name__ == '__main__':
    main()
