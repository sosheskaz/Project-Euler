using System.Collections.Generic;
using System.Linq;
using System;

namespace EulerUtils
{
    public class Sieve
    {
        public static List<long> GetSieve(long lim) {
            bool[] sieve = new bool[lim + 1];

            for (long x = 1L; ; x++)
            {
                long x2 = x * x;
                if (x2 > lim) break;

                for(long y = 1L; ; y++)
                {
                    long y2 = y * y;
                    if (y2 > lim) break;

                    long n = 4 * x2 + y2;
                    if (n <= lim && (n % 12 == 1 || n % 12 == 5))
                    {
                        sieve[n] ^= true;
                    }

                    n = 3 * x2 + y2;
                    if (n <= lim && n % 12 == 7)
                    {
                        sieve[n] ^= true;
                    }

                    n = 3 * x2 - y2;
                    if (n <= lim && x2 > y2 && n % 12 == 11)
                    {
                        sieve[n] ^= true;
                    }
                }
            }

            for (long r = 5; r * r <= lim; r += 2)
            {
                if (sieve[r]) {
                    long s = r * r;
                    for(long k = s; k <= lim; k += s)
                    {
                        sieve[k] = false;
                    }
                }
            }

            sieve[2] = sieve[3] = true;

            var primes = new List<long>();
            for (long i = 2; i < sieve.Length; i++) {
                if (sieve[i]) {
                    primes.Add(i);
                }
            }

            return primes;
        }
    }
}
