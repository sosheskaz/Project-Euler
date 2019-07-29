#!/usr/bin/env python3
from itertools import takewhile, combinations_with_replacement
import math
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    target = 28123
    abundants = list(takewhile(lambda x: x <= target, abundant_numbers()))
    abundant_sums = {sum(pair)
                     for pair in combinations_with_replacement(abundants, 2)
                     if sum(pair) <= target}
    sum_of_abundant_sums = sum(abundant_sums)

    sum_of_all = (target + 1) // 2 * target

    sum_of_non_abundant_sums = sum_of_all - sum_of_abundant_sums

    print(sum_of_non_abundant_sums)


def abundant_numbers():
    n = 1
    while True:
        if is_abundant(n):
            yield n
        n += 1


def is_abundant(n):
    return sum(get_factors(n)) > n


def get_factors(n):
    limit = int(math.floor(math.sqrt(n))) + 1
    yield 1
    for i in range(2, limit):
        div, mod = divmod(n, i)
        if mod == 0:
            yield div
            if div * div != n:
                yield n // div


if __name__ == '__main__':
    main()
