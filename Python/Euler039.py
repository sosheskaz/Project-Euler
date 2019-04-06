#!/usr/bin/env python3
import math
__author__ = 'ericmiller'


def main():
    all_squares = get_primes(1000)

    longest = 0
    longest_value = 0

    for i in range(1, 1000):
        count = 0
        for square1 in all_squares:
            if square1[0] >= i:
                continue

            for square2 in all_squares:
                if square1[0] + square2[0] >= i:
                    break

                side3_restriction = i - square1[0] - square2[0]
                side3_pythagorean = math.sqrt(square1[1] + square2[1])

                if side3_restriction == side3_pythagorean:
                    count += 1

        if count > longest_value:
            longest = i
            longest_value = count

    print(longest)
    print(longest_value)


def get_primes(maximum):
    all_squares = list()

    for i in range(1, maximum):
        all_squares.append((i, i * i))

    return all_squares

main()
