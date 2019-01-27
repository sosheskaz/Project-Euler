#!/usr/bin/env python
from __future__ import print_function


def main():
    print(list(prime_factors(600851475143))[-1])


def prime_factors(of_number):
    while not (of_number % 2):
        of_number /= 2
        yield 2

    for i in xrange(3, of_number, 2):
        if of_number == 1:
            break

        while of_number % i == 0:
            of_number /= i
            yield i


if __name__ == '__main__':
    main()
