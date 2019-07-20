#!/usr/bin/env python3
from itertools import chain
import math
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    target = 10000
    proper_divisors_sums = {}
    amicable_sum = 0

    for i in range(1, target):
        if i not in proper_divisors_sums:
            proper_divisors_sums[i] = get_proper_divisors_sum(i)
        divisors_sum = proper_divisors_sums[i]

        if divisors_sum not in proper_divisors_sums:
            proper_divisors_sums[divisors_sum] = get_proper_divisors_sum(divisors_sum)
        other_divisors_sum = proper_divisors_sums[divisors_sum]

        if other_divisors_sum == i and i != divisors_sum:
            amicable_sum += i

    print(amicable_sum)


def get_proper_divisors_sum(n):
    limit = math.ceil(math.sqrt(n)) + 1
    nums = ((i, n // i) for i in range(2, limit + 1) if n % i == 0)
    return sum(set(chain(*nums))) + 1


if __name__ == '__main__':
    main()
