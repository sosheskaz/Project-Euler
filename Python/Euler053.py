#!/usr/bin/env python3
import itertools
import sympy
from tqdm import tqdm


def main():
    count = 0
    for n in tqdm(range(100, 0, -1)):
        result = count_over_1m_for_n(n)
        if result == 0:
            break
        count += result
    print(count)


def count_over_1m_for_n(n):
    count = 0
    for r in middle_out(range(1, n)):
        if num_combinations(n, r) > 1000000:
            count += 1
    return count


def num_combinations(n, r):
    return sympy.factorial(n) / sympy.factorial(r) / sympy.factorial(n - r)


def middle_out(of_list):
    if not isinstance(of_list, list):
        of_list = list(of_list)
    range1 = iter(of_list[:(len(of_list) // 2)])
    range2 = iter(of_list[(len(of_list) // 2):])
    overall_range = range(0, len(of_list))
    for i in overall_range:
        if i % 2 == 0:
            yield next(range2)
        else:
            yield next(range1)


if __name__ == '__main__':
    main()
