#!/usr/bin/env python3
from math import sqrt, floor, ceil

def main():
    target = 1000
    for a in range(3, ceil((target - 1) / 3)):
        for b in range(a + 1, ceil(target - a / 2)):
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
