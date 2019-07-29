#!/usr/bin/env python3


num_cache = {}
den_cache = {}


def main():
    populate_caches()
    meet_criteria = [(d, get_numerator(d), get_denominator(d)) for d in range(1, 1001) if is_num_longer_than_den(d)]
    print(len(meet_criteria))


def populate_caches():
    num_cache[1] = 1
    num_cache[2] = 1
    den_cache[1] = 1
    den_cache[2] = 2


def is_num_longer_than_den(depth):
    num = get_numerator(depth)
    den = get_denominator(depth)
    num_len = len(str(num))
    den_len = len(str(den))
    return num_len > den_len


def get_numerator(depth):
    return reusable_recursion(num_cache, depth + 2)


def get_denominator(depth):
    return reusable_recursion(den_cache, depth + 1)


def reusable_recursion(cache, depth):
    if depth in cache:
        return cache[depth]
    if depth < 3:
        raise Exception('recursion error for depth {}'.format(depth))
    cache[depth] = (2 * reusable_recursion(cache, depth-1)) + reusable_recursion(cache, depth-2)
    return cache[depth]


if __name__ == '__main__':
    main()


