#!/usr/bin/env python3
import itertools
import sympy


def main():
    primegen = generate_primes()
    squaregen = generate_square2()
    primes = set([next(primegen)])
    maxprime = 2
    square2s = [next(squaregen)]
    maxsquare = square2s[0]
    current = 9
    for line in open('composite.txt'):
        c = int(line)
        while maxprime < c:
            maxprime = next(primegen)
            primes.add(maxprime)
        while maxsquare < c:
            maxsquare = next(squaregen)
            square2s.append(maxsquare)
        if breaks_conjecture(c, square2s, primes):
            print(c)
            return


def breaks_conjecture(number, square2s, primes):
    for s in reversed(square2s):
        if (number - s) in primes:
            return False
    return True


def generate_primes():
    for i in sympy.sieve:
        yield i


def generate_square2():
    current = 1
    while True:
        yield 2 * current * current
        current += 1


if __name__ == '__main__':
    main()
