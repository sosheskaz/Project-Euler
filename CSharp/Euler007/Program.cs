using System;
using EulerUtils;

namespace Euler007
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Sieve.GetSieve(200000)[10001]);
        }
    }
}
