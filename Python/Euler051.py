#!/usr/bin/env python3
import itertools
from sympy import isprime, sieve
from tqdm import tqdm


def main():
    answer = None
    for prime in tqdm(sieve):
        family = get_prime_family(prime)
        if len(family) == 8:
            answer = family
            break
    print()
    print(sorted(answer))


def get_prime_family(of_prime):
    base = of_prime
    base_str = str(base)
    combinations = itertools.chain.from_iterable(itertools.combinations(set(range(0, len(base_str))), i) for i in range(1, len(base_str)))

    replace_digits = [str(digit) for digit in range(0, 10)]
    family = set()
    for combo in combinations:
        cur_family = set()
        for replace_digit in replace_digits:
            test_str = list(base_str)
            for index in combo:
                test_str[index] = replace_digit
            asint = int(''.join(test_str))
            if asint < of_prime:
                continue
            if isprime(asint):
                cur_family.add(asint)
        if len(cur_family) > len(family):
            family = cur_family
    return family


if __name__ == '__main__':
  main()
