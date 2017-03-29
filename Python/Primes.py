__author__ = 'ericmiller'


def get_primes(max):
    if max < 3:
        return -1
    known_primes = list()
    known_primes.append(2)
    known_primes.append(3)
    index = 4
    for i in range(index, o):
        is_prime = True

        for prime in known_primes:
            if index % prime == 0:
                is_prime = False
                break

        if is_prime:
            known_primes.append(index)
