using System.Linq;
using System;
using EulerUtils;

namespace Euler005
{
    class Program
    {
        private const long target = 20;

        static void Main(string[] args)
        {
            var product = Sieve.GetSieve(target)
                .Select((prime) => (long) Math.Pow(prime, Math.Floor(Math.Log(target, prime))))
                .Aggregate((subProduct, n) => subProduct * n);

            Console.WriteLine(product);
        }
    }
}
