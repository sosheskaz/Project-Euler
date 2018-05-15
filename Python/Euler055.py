#!/usr/bin/env python3
import multiprocessing
import joblib

def main():
    # Overhead makes parallel slightly slower at this level.
    # Increasing n increases the effectiveness of parallel.
    parallel(10000)


def serial(n):
    results = (is_lychrel(i) for i in range(1, n))
    print(sum(results))

def parallel(n):
    is_lych = joblib.delayed(is_lychrel)
    results = joblib.Parallel(multiprocessing.cpu_count())(is_lych(i) for i in range(1, n))
    print(sum(results))


def is_lychrel(number):
    active_val = number
    for i in range(0, 50):
        active_val = active_val + reversed_num(active_val)
        if is_palindrome(active_val):
            return False
    return True


def is_palindrome(number):
    as_str = str(number)
    return as_str == ''.join(reversed(as_str))

def reversed_num(number):
    return int(''.join(reversed(str(number))))


if __name__ == '__main__':
    main()
