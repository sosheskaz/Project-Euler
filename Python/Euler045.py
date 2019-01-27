#!/usr/bin/env python3
import math
from Euler044 import is_pentagonal


def main():
    for i in generate_hexagonal_numbers():
        if not is_triangular(i):
            continue
        if not is_pentagonal(i):
            continue
        if i <= 40755:
            continue
        print(i)
        return


def is_triangular(number):
    return math.sqrt(8 * number + 1) % 1 == 0


def generate_hexagonal_numbers():
    counter = 5
    value = 1
    while True:
        yield value
        value += counter
        counter += 4


if __name__ == '__main__':
    main()
