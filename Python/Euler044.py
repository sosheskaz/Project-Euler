#!/usr/bin/env python3
import math


def main():
    nums = list()
    for p in generate_pentagonal_numbers():
        checkables = [(p, n) for n in nums]
        nums.append(p)
        for pair in checkables:
            if not is_pentagonal(pair[0] - pair[1]):
                continue
            if not is_pentagonal(pair[0] + pair[1]):
                continue
            print(pair[0] - pair[1])


def generate_pentagonal_numbers():
    counter = 4
    value = 1
    while True:
        yield value
        value += counter
        counter += 3


def is_pentagonal(number):
    return math.sqrt(24 * number + 1) % 6 == 5


if __name__ == '__main__':
    main()
