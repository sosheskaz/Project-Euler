using System.Numerics;
using System;
using Combinatorics;

namespace Euler020
{
    class Program
    {
        private const int target = 100;
        private static readonly BigInteger big10 = new BigInteger(10);

        static void Main(string[] args)
        {
            var result = Combo.Factorial(new BigInteger(target));
            int s = 0;

            while (result > 0)
            {
                int digit = (int)(result % big10);
                s += digit;
                result /= big10;
            }

            Console.WriteLine(s);
        }
    }
}
