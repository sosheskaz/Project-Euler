#!/usr/bin/env python3
# Uses john the ripper password list to guess passwords
from itertools import permutations, cycle
import os
from joblib import Parallel, delayed


# We need this to be global for multiprocessing to work efficiently
with open('p042_words.txt') as dictionary_f:
    dictionary = {word.strip('"').lower()
                  for word in dictionary_f.read().split(',')}
with open('p059_cipher.txt') as cipher_f:
    cipher_t = [int(ord_str) for ord_str in cipher_f.read().split(',')]


def main():
    combos = permutations(range(ord('a'), ord('z') + 1), 3)
    results = Parallel(n_jobs=os.cpu_count())(
            delayed(check_candidate)(key) for key in combos)
    good_results = (tup for tup in results if tup[0])
    for _, raw, as_str, key in good_results:
        print('Found decryption candidate "{}"'.format(key))
        print(as_str)
        print('Answer: {}'.format(sum(raw)))


def check_candidate(key):
    decrypt_attempt = xor_ords(cipher_t, key)
    as_str = ''.join(chr(i) for i in decrypt_attempt)
    as_words = {word.strip().lower() for word in as_str.split(' ')}
    recognized_words = dictionary.intersection(as_words)

    is_viable_candidate = as_str.isprintable() and len(recognized_words) / len(set(as_words)) > 0.1
    printable_key = ''.join(chr(i) for i in key)
    return is_viable_candidate, decrypt_attempt, as_str, printable_key


def xor_ords(cipher_t, key):
    if isinstance(cipher_t, str):
        cipher_t = [ord(c) for c in cipher_t]
    if isinstance(key, str):
        key = [ord(c) for c in key]
    return [c1 ^ c2 for c1, c2 in zip(cipher_t, cycle(key))]


if __name__ == '__main__':
    main()
