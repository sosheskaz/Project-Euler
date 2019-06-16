#!/usr/bin/env python3
from __future__ import print_function
from datetime import datetime
import sys
if sys.version.startswith('2'):
    range = xrange


def main():
    sunday = 6
    sundays = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            d = datetime(year, month, 1)
            if d.weekday() == sunday:
                sundays += 1

    print(sundays)


if __name__ == '__main__':
    main()
