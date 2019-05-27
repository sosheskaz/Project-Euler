using System;
using System.Linq;
using EulerUtils;

namespace Euler010
{
    class Program
    {
        private const long target = 2000000;

        static void Main(string[] args)
        {
            var primes = Sieve.GetSieve(target);
            long sum = primes.Sum();
            Console.WriteLine(sum);
        }
    }
}
