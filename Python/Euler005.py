#!/usr/bin/env python
from __future__ import print_function
from operator import mul
from itertools import groupby


def main():
    factorizations = (prime_factors(i) for i in xrange(2, 21))
    frequencies = {}
    for factorization in factorizations:
        tmp_frequencies = {prime: len(list(freq)) for prime, freq in groupby(factorization)}
        to_overwrite = {key: value
                        for key, value in tmp_frequencies.items()
                        if key not in frequencies or value > frequencies[key]}
        frequencies.update(to_overwrite)

    sub_products = (factor ** freq for factor, freq in frequencies.items())
    product = reduce(mul, sub_products)
    print(product)


def prime_factors(of_number):
    while not (of_number % 2):
        of_number /= 2
        yield 2

    for i in xrange(3, of_number + 1, 2):
        if of_number == 1:
            break

        while of_number % i == 0:
            of_number /= i
            yield i


if __name__ == '__main__':
    main()
