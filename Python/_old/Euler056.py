#!/usr/bin/env python3
import itertools
import joblib


def main():
    # By n=200, parallel is much faster.
    parallel(100)

def serial(n):
    xy_combos = ((x, y) for x in range(1, n) for y in range(1, n))
    print(max(get_digit_sum(x, y) for x, y in xy_combos))


def parallel(n):
    xy_combos = ((x, y) for x in range(1, n) for y in range(1, n))
    digit_sum = joblib.delayed(get_digit_sum)
    results = joblib.Parallel(joblib.cpu_count()*2)(digit_sum(x, y) for x, y in xy_combos)
    print(max(results))


def get_digit_sum(x, y):
    as_str = str(x ** y)
    return sum(int(c) for c in as_str)


if __name__ == '__main__':
    main()
