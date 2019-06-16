#!/usr/bin/env python3
from __future__ import division, print_function
from math import sqrt, floor, ceil
import sys
if sys.version.startswith('2'):
    range = xrange

def main():
    target = 1000
    for a in range(3, int(ceil((target - 1) / 3))):
        for b in range(a + 1, int(ceil(target - a / 2))):
            c = sqrt(a*a + b*b)
            if c == floor(c):
                c = int(c)
                s = a + b + c

                factor, mod = divmod(target, s)
                if mod is 0:
                    aFinal = factor * a
                    bFinal = factor * b
                    cFinal = factor * c

                    print(aFinal * bFinal * cFinal)
                    return
                else:
                    break

if __name__ == '__main__':
    main()
