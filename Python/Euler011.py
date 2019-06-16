#!/usr/bin/env python
from __future__ import print_function
from functools import reduce
from operator import mul
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    target = 4
    table = [row for row in load_file('input/Euler011.txt')]
    biggest = max_product(table, target)
    print(biggest)


def load_file(path):
    with open(path) as f:
        return [[int(num) for num in line.split(' ')]
                for line in f.readlines() if line]


def max_product(table, target):
    biggest = -1

    for i in range(0, len(table)):
        for j in range(target-1, len(table)):
            diag_e, diag_w = (-1, -1)

            horiz = reduce(mul, (table[i][j-cursor]
                    for cursor in range(0, target)))
            vert = reduce(mul, (table[j-cursor][i]
                    for cursor in range(0, target)))

            if i >= target:
                diag_e = reduce(mul, (table[i-cursor][j-cursor]
                        for cursor in range(0, target)))
            if j <= len(table[0]) - target:
                diag_w = reduce(mul, (table[i-cursor][j+cursor]
                        for cursor in range(0, target)))

            biggest = max(*(biggest, horiz, vert, diag_e, diag_w))

    return biggest



if __name__ == '__main__':
    main()
