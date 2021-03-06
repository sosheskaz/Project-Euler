#!/usr/bin/env python3
from __future__ import print_function
from functools import reduce
from itertools import count, takewhile
from math import log
from operator import mul


def main():
    n = 20
    primes = takewhile(lambda x: x <= n, get_primes())
    prime_pow = lambda prime, ceiling: prime ** int(log(ceiling, prime))
    result = reduce(mul, (prime_pow(prime, n) for prime in primes))
    print(result)


def get_primes():
    yield 2
    prime_checker = []
    for i in count(3, 2):
        if all(i % prev_prime for prev_prime in prime_checker):
            yield i
            prime_checker.append(i)


if __name__ == '__main__':
    main()
