#!/usr/bin/env python3
import math


def main():
    target = 20
    print(combinatoric(target * 2, target))


def combinatoric(n, r):
    numer = math.factorial(n)
    denom = math.factorial(r) * math.factorial(n - r)
    return numer // denom


if __name__ == '__main__':
    main()
