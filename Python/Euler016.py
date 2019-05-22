#!/usr/bin/env python3


def main():
    target = 1000

    x = 2 ** target
    s = 0

    while x > 0:
        x, mod = divmod(x, 10)
        s += mod

    print(s)



if __name__ == '__main__':
    main()
