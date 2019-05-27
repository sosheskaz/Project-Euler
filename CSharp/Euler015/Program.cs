using System.Numerics;
using System;
using Combinatorics;

namespace Euler015
{
    class Program
    {
        private static readonly BigInteger target = 20;

        static void Main(string[] args)
        {
            Console.WriteLine(Combo.Combinations(target * 2L, target));
        }
    }
}
