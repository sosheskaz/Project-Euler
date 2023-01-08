#!/usr/bin/env python3
import itertools


def main():
    target = 1000
    prime_nums = itertools.takewhile(lambda p: p < target, primes())
    # print(list(prime_nums))

    print(max(remainder_2_5(i) for i in prime_nums))


def remainder_2_5(a):
    result = a
    while not result % 5:
        result /= 5
    while not result % 2:
        result /= 2
    return result

def primes():
    yield 2
    primes = [2]
    test = 3
    while True:
        if all(test % p for p in primes):
            primes.append(test)
            yield test
        test += 2


main()
