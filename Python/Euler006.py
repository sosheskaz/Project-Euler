#!/usr/bin/env python3

def main():
    n = 101
    sum_of_squares = sum(i ** 2 for i in range(1, n))
    square_of_sum = sum(range(1, n)) ** 2
    print(square_of_sum - sum_of_squares)


if __name__ == '__main__':
    main()
