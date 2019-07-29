#!/usr/bin/env python3


def main():
    print(sum(get_fancy_pandigitals()))


def get_fancy_pandigitals():
    primes = [2, 3, 5, 7, 11, 13, 17]
    for p in [p for p in get_permutations() if p >= 10**9]:
        ps = str(p)
        valid = True
        for i, prime in enumerate(primes, 1):
            new = int(ps[i:i+3])
            if new % prime != 0:
                valid = False
            continue
        if valid:
            yield p


def get_permutations(prefix='', values=[str(i) for i in range(0, 10)]):
    if len(values) < 1 and prefix != '':
        yield int(prefix)

    for v in values:
        next_prefix = prefix + str(v)
        next_values = list(filter(lambda v2: v2 != v, values))
        for item in get_permutations(next_prefix, next_values):
            yield item


if __name__ == '__main__':
    main()
