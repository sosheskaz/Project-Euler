using System.Numerics;
using System;

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
    }
}
