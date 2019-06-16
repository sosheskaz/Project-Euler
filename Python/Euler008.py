#!/usr/bin/env python3
from __future__ import print_function
from functools import reduce
from math import sqrt
from operator import mul

def main():
    factor_ct = 13
    char0 = 48

    with open('input/Euler008.txt') as f:
        contents = [ord(c) - char0 for c in f.read() if '0' <= c <= '9']

    buffer = [0] * factor_ct

    product = 0
    for index, value in enumerate(contents):
        buffer[index % factor_ct] = value
        product = max(product, reduce(mul, buffer))

    print(product)


if __name__ == '__main__':
    main()
