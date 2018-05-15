#!/usr/bin/env python3
import itertools
from tqdm import tqdm

MULTIPLIER_RANGE = range(2, 7)


def main():
    for i in tqdm(itertools.count(1)):
        if test_number(i):
            print()
            print(i)
            return


def test_number(num):
    for multiplier in MULTIPLIER_RANGE:
        if not test_multiplier(num, multiplier):
            return False
    return True


def test_multiplier(base, multiplier):
    product = base * multiplier
    return set(str(base)) == set(str(product))


if __name__ == '__main__':
    main()
