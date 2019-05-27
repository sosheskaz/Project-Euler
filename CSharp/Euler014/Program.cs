using System.Linq;
using System.Collections.Generic;
using System;

namespace Euler014
{
    class Program
    {
        private const int target = 1000000;

        static void Main(string[] args)
        {
            var chains = Enumerable.Range(1, target).AsParallel().Select(n => Collatz(n).ToList());
            long biggestN = -1;
            int biggestCount = -1;
            foreach(var chain in chains)
            {
                int ct = chain.Count;
                if (ct > biggestCount)
                {
                    biggestCount = ct;
                    biggestN = chain.First();
                }
            }
            Console.WriteLine(biggestN);
        }

        static IEnumerable<long> Collatz(int n)
        {
            return Collatz((long) n);
        }

        static IEnumerable<long> Collatz(long n)
        {
            while (n > 1L)
            {
                yield return n;
                if (n % 2L == 0L)
                {
                    n /= 2L;
                }
                else
                {
                    n = 3L * n + 1L;
                }
            }

            yield return n;
        }
    }
}
