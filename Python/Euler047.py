#!/usr/bin/env python3
from sympy.ntheory import primefactors


def main():
    lastfew = []
    for i in range(2, 2**32):
        factors = primefactors(i)
        if len(factors) == 4:
            lastfew.append(i)
        else:
            lastfew = []
        if len(lastfew) == 4:
            print(lastfew[0])
            return


if __name__ == '__main__':
    main()
