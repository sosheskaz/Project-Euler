#!/usr/bin/env python3
import itertools
import joblib
import math
import multiprocessing
from sympy import sieve


def main():
    primes = list(sieve.primerange(1000, 10000))
    combos = set()
    ignore = {'148748178147'}
    # This is really inefficient, but it's a small enough data set that it works.
    # for prime in primes:
    func = joblib.delayed(check_combos_for)
    parallelism = multiprocessing.cpu_count()
    combos.update(itertools.chain.from_iterable(joblib.Parallel(parallelism)(func(prime, primes) for prime in primes)))
    combos.difference_update(ignore)
    for combo in combos:
        print(combo)

def check_combos_for(prime, primelist):
    cprime = set(str(prime))
    matches = {p for p in primelist if p > prime and set(str(p)) == cprime}
    return ['{}{}{}'.format(*trio)
                        for trio in itertools.combinations(sorted(matches), 3)
                        if trio[2] - trio[1] == trio[1] - trio[0]]


if __name__ == '__main__':
    main()
