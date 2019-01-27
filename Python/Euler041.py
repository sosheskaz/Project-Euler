import sympy
from tqdm import tqdm

def get_permutations(prefix='', values=[str(i) for i in range(1, 10)]):
    if len(values) < 1 and prefix != '':
        yield int(prefix)

    for v in values:
        next_prefix = prefix + str(v)
        next_values = list(filter(lambda v2: v2 != v, values))
        for item in get_permutations(next_prefix, next_values):
            yield item


biggest = 0
values = map(lambda max: range(1, max), range(2, 11))
for r in values:
    for item in tqdm(get_permutations(values=list(r))):
        if item > biggest:
            if sympy.isprime(item):
                biggest = item

print(biggest)
