using System.Linq;
using System.Collections.Generic;
using System;

namespace Euler003
{
    class Program
    {
        static void Main(string[] args)
        {
            var factors = primeFactors(600851475143);
            Console.WriteLine(factors.Last());
        }

        static IEnumerable<long> primeFactors(long n) {
            while (n % 2 == 0) {
                n /= 2;
                yield return n;
            }

            for (int i = 3; i <= n; i += 2) {
                if (n == 1) {
                    break;
                }

                while (n % i == 0) {
                    n /= i;
                    yield return i;
                }
            }
        }
    }
}
