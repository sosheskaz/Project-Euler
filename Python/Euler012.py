#!/usr/bin/env python3
from itertools import chain
import math
import os


def main():
    target = 500

    triangles = triangle_numbers()
    factors = ((t, get_factors(t)) for t in triangles)
    gt_target = (tup for tup in factors if len(tup[1]) >= target)
    print(next(gt_target)[0])


def get_factors(of_int: int):
    max_low_factor = int(math.sqrt(of_int)) + 1
    low_factors = {i for i in range(1, max_low_factor) if of_int % i == 0}
    high_factors = {of_int//i for i in low_factors}
    return low_factors.union(high_factors)


def triangle_numbers():
    i = 0
    incrementer = 1
    while True:
        i += incrementer
        yield i
        incrementer += 1


if __name__ == '__main__':
    main()
