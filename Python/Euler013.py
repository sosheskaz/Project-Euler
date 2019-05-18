#!/usr/bin/env python3


def main():
    digits = 10
    infile = 'input/Euler013.txt'

    nums = parse_file(infile)
    numsum = sum(nums)

    print(str(numsum)[:digits])


def parse_file(path) -> list:
    with open(path) as f:
        return [int(num) for num in f.readlines()]


if __name__ == '__main__':
    main()
