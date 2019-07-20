using System.Collections.Generic;
using System.Linq;
using System;

namespace Euler021
{
    class Program
    {
        private const int target = 10000;

        static void Main(string[] args)
        {
            int amicableSum = 0;
            var properDivisorsSums = new Dictionary<int, int>(target);

            foreach (int i in Enumerable.Range(1, target - 1))
            {
                if (!properDivisorsSums.ContainsKey(i))
                {
                    properDivisorsSums[i] = ProperDivisorsSum(i);
                }
                int divisorsSum = properDivisorsSums[i];

                if (!properDivisorsSums.ContainsKey(divisorsSum))
                {
                    properDivisorsSums[divisorsSum] = ProperDivisorsSum(divisorsSum);
                }
                int otherDivisorsSum = properDivisorsSums[divisorsSum];

                if (otherDivisorsSum == i && i != divisorsSum)
                {
                    amicableSum += i;
                }
            }

            Console.WriteLine(amicableSum);
        }

        static int ProperDivisorsSum(int n)
        {
            int sum = 1;
            int lim = (int)Math.Ceiling(Math.Sqrt(n));

            foreach(int i in Enumerable.Range(2, lim - 1))
            {
                if (n % i != 0)
                    continue;
                sum += i;
                if (n != lim)
                {
                    sum += n / i;
                }
            }

            return sum;
        }
    }
}
