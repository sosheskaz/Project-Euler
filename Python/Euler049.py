from sympy import sieve


def main():
    primes = [i for i in sieve.primerange(1000, 10000) if len(set(str(i))) == 4]
    # This is really inefficient, but it's a small enough data set that it works.
    for prime in primes:
        ps = str(prime)
        matches = [ps]
        for prime2 in [str(p) for p in primes if p > prime]:
            has_match = True
            for c in prime2:
                if c not in ps:
                    has_match = False
                    break
            if has_match:
                matches.append(prime2)
        if len(matches) >= 3:
            for i, e1 in enumerate(matches[0:]):
                for e2 in matches[i+1:]:
                    if str(2 * int(e2) - int(e1)) in matches:
                        print([e1, e2, str(2 * int(e2) - int(e1))])


if __name__ == '__main__':
    main()
