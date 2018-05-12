#!/usr/bin/env python3
from sympy import sieve, isprime
from tqdm import tqdm

def main():
    ceiling = 1000000

    summable_primes = list(sieve.primerange(0, ceiling))
    con = next(get_valid_consecutives(summable_primes, ceiling))
    print(sum(con))
    # max_n_terms = len(summable_primes)
    # print (max_n_terms)
    # for n_terms in range(max_n_terms//3, 0, -1):
    #     tuples = ((np.sum(combo), combo) for combo in itertools.combinations(summable_primes, n_terms))
    #     items = (pair[1] for pair in tuples if pair[0] < ceiling and isprime(pair[0]))
    #     for combo in items:
    #         print('{}: {} -> {}'.format(len(combo), combo, sum(combo)))
    #         return

def get_valid_consecutives(primelist, maximum):
    primelist_reversed = sorted(primelist, reverse=True)
    for sublist_size in tqdm(range(len(primelist)+1, 0, -1)):
        if sum(primelist_reversed[len(primelist)-sublist_size:]) >= maximum:
            continue
        for left_padding in range(0, len(primelist)-sublist_size+1):
            right_padding = sublist_size + left_padding
            sublist = primelist_reversed[left_padding:right_padding]
            con_sum = sum(sublist)
            if con_sum >= maximum or not isprime(con_sum):
                continue
            yield sublist


if __name__ == '__main__':
    main()
