#!/usr/bin/env python3
from __future__ import print_function
from itertools import combinations


def main():
    combos = combinations(range(100, 1000), 2)
    product_strings = (str(x * y) for x, y in combos)
    palindromes = (int(s) for s in product_strings if s == s[::-1])
    biggest = max(palindromes)
    print(biggest)


if __name__ == '__main__':
    main()
