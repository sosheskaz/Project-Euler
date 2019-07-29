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

        public static IEnumerable<IEnumerable<T>> GetCombinationsWithReplacement<T>(List<T> l, int count) {
            if (count < 1) {
                return new List<List<T>>();
            }

            if (count == 1) {
                return from i in l select new T[]{i};
            } else {
                return l.AsParallel()
                    .Select(
                        (item, index) => GetCombinationsWithReplacement(l.GetRange(index, l.Count - index), count - 1).Select(combo => combo.Concat(new T[]{item}))
                    ).SelectMany(x => x.ToList());
            }
        }
    }
}
