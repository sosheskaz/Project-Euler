#!/usr/bin/env python3
from __future__ import print_function
import re


BASE_LETTER_SCORE = ord('a') - 1


def main():
    names = sorted(read_file('input/names.txt'))
    scores = (score_name(name) * idx for idx, name in enumerate(names, 1))
    final_score = sum(scores)
    print(final_score)


def read_file(path):
    with open(path) as f:
        return (re.sub(r'\W', '', name) for name in f.read().split(','))


def score_name(name):
    return sum(score_letter(c) for c in name.lower())


def score_letter(c):
    return ord(c) - BASE_LETTER_SCORE

if __name__ == '__main__':
    main()
