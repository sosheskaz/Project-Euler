import itertools
import math
import sys
if sys.version.startswith('2'):
    range = xrange

def sieve(lim):
    sieve = [False] * (lim + 1)
    sqrt = math.sqrt(lim)
    ceil = int(math.ceil(math.sqrt(lim)))
    if int(sqrt) != ceil:
        ceil += 1

    square_range = [i * i for i in range(1, ceil)]
    for x2, y2 in itertools.product(square_range, square_range):
        n = 4 * x2 + y2
        if n <= lim and n % 12 in (1, 5):
            sieve[n] ^= True

        n = 3 * x2 + y2
        if n <= lim and n % 12 == 7:
            sieve[n] ^= True

        n = 3 * x2 - y2
        if n <= lim and x2 > y2 and n % 12 == 11:
            sieve[n] ^= True

    for i in (2, 3):
        sieve[i] = True

    for r in range(5, ceil, 2):
        if sieve[r]:
            s = r * r
            for k in range(s, lim, s):
                sieve[k] = False

    return [index for index, is_prime in enumerate(sieve) if is_prime]
