#!/usr/bin/env python3
from sympy import isprime

def main():
    spirals = spiral_numbers()
    prime_spirals = {True: [], False: []}
    side_length = -1
    while True:
        # Throttle the infinite iterator so we can assess it in bits
        next4 = (next(spirals) for _ in range(4))
        for length, i in next4:
            prime_spirals[isprime(i)].append(i)
            side_length = length
        if len(prime_spirals[True]) * 9 <= len(prime_spirals[False]):
            print('Side length at cutoff point is {}'.format(side_length))
            return 0


def spiral_numbers():
    # Starting from 0 would give us 4 repeats.
    side_l = 2
    iterations = (1, 2, 3, 4)
    counter = 0
    while True:
        for _ in iterations:
            counter += side_l
            yield (side_l + 1, counter + 1)
        side_l += 2


if __name__ == '__main__':
    exit(main())
