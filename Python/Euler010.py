#!/usr/bin/env python3
import sieve


def main():
    target = 2000000
    primes = sieve.sieve(target)
    print(sum(primes))


if __name__ == '__main__':
    main()
