using System.Numerics;
using System;
using System.Linq;
using System.Collections.Generic;

namespace Combinatorics
{
    public partial class Combo
    {
        public static long Combinations(long n, long r)
        {
            long numer = Factorial(n);
            long denom = Factorial(r) * Factorial(n - r);
            return numer / denom;
        }

        public static BigInteger Combinations(BigInteger n, BigInteger r)
        {
            BigInteger numer = Factorial(n);
            BigInteger denom = Factorial(r) * Factorial(n - r);
            return numer / denom;
        }

        public static IEnumerable<IList<T>> GetCombinationsWithReplacement<T>(IList<T> pool, int r) {
            var n = pool.Count();
            var indices = Enumerable.Range(0, r).Select(_ => 0).ToArray();
            int i = 0;

            var current = indices.Select((idx) => pool[idx]).ToList();
            yield return current;

            for (;;)
            {
                i = r - 1 - Enumerable.Range(1, r).Select(x => r - x).TakeWhile(idx => indices[idx] == n - 1).Count();
                if (i < 0)
                    break;

                indices[i]++;

                for (var idx = i + 1; idx < r; idx++) {
                    indices[idx] = indices[i];
                }

                current = indices.Select(idx => pool[idx]).ToList();
                yield return current;
            }
        }
    }
}
