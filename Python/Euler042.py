import math


def is_triangular(n):
    return ((math.sqrt(8*n + 1) - 1) / 2) % 1 == 0


with open('p042_words.txt', 'r') as f:
    base = ord('A') - 1
    raw = f.readline()
    noq = raw.replace('"', '')
    vals = noq.split(',')
    ct = 0
    for v in vals:
        tri = 0
        for c in v:
            tri += ord(c) - base
        if is_triangular(tri):
            ct += 1

    print(ct)
