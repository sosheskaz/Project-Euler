#!/usr/bin/env python3
from __future__ import print_function
import sys
if sys.version.startswith('2'):
    range = xrange

def main():
    print(max(prime_factors(600851475143)))


def prime_factors(of_number):
    div, mod = divmod(of_number, 2)
    while mod is 0:
        of_number = div
        yield 2
        div, mod = divmod(of_number, 2)

    for i in range(3, of_number, 2):
        if of_number is 1:
            break

        div, mod = divmod(of_number, i)
        while mod is 0:
            of_number = div
            yield i
            div, mod = divmod(of_number, i)


if __name__ == '__main__':
    main()
