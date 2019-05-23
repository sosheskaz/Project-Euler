#!/usr/bin/env python3
from math import factorial


def main():
    target = 100
    result = factorial(target)
    s = 0

    while result > 0:
        result, digit = divmod(result, 10)
        s += digit

    print(s)


if __name__ == '__main__':
    main()
