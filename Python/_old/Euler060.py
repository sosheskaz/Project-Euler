#!/usr/bin/env python3
from itertools import chain, combinations, permutations, zip_longest
import os
from joblib import delayed, Parallel
from sympy import sieve, isprime
from tqdm import tqdm

# I don't have a good idea for how to solve this, so brute force it is.
def main():
    assert test_concatenations((3, 7, 109, 673))

    # This doesn't parallelize well with joblib. CPU performance can be okay,
    # but memory usage explodes because it needs to calculate all the
    # combinations up front. A workaround could be made, but that's more effort
    # than I want for this one.
    combos = tqdm(combinations(sieve.primerange(0, 5000), 5))
    raw = (test_concatenations(combo) for combo in combos)
    pruned = (result for result in raw if result[0])
    print(min(pruned), lambda x: x[1])


def test_concatenations(combination):
    '''Returns true if all pair concatenations of this combination are prime'''
    sub_pairs = permutations(combination, 2)
    test = all(isprime(int('{}{}'.format(c[0], c[1]))) for c in sub_pairs)
    # Calculate the sum in the parallel block
    c_sum = sum(combination) if test else 2000000000
    # Returning the input back is convenient for parallel
    return (test, c_sum, combination)


if __name__ == '__main__':
    main()
