using System.Numerics;
using System;

namespace Euler016
{
    class Program
    {
        private const int target = 1000;
        private static readonly BigInteger big10 = 10;

        static void Main(string[] args)
        {
            var x = BigInteger.Pow(2, target);
            int s = 0;

            while (x > 0)
            {
                int mod = (int)(x % big10);
                s += mod;
                x /= big10;
            }

            Console.WriteLine(s);
        }
    }
}
