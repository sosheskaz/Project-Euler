#!/usr/bin/env python3
from __future__ import print_function
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    target = 1000
    print(sum(len(word_for_number(n)) for n in range(1, target + 1)))


def word_for_number(n):
    word = ''
    if n >= 1000000:
        raise "Error: Number was too big: %d" % n
    if n >= 1000:
        word += word_for_number(n // 1000) + 'thousand'
        n %= 1000
    if n >= 100:
        word += word_for_number(n // 100) + 'hundred'
        n %= 100
        if n != 0:
            word += 'and'

    tens_map = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }
    nmod10 = n // 10
    if nmod10 in tens_map:
        word += tens_map[nmod10]
    if n >= 20:
        n %= 10

    ones_map = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    word += ones_map[n]

    return word


if __name__ == '__main__':
    main()
