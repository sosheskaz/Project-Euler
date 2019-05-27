using System.Linq;
using System.Collections.Generic;
using System;

namespace Euler006
{
    class Program
    {
        private const int target = 100;

        static void Main(string[] args)
        {
            var squareOfSum = SquareOfSum(Enumerable.Range(1, target));
            var sumOfSquares = SumOfSquares(Enumerable.Range(1, target));
            Console.WriteLine(squareOfSum - sumOfSquares);
        }

        private static int SumOfSquares(IEnumerable<int> nums)
        {
            return nums.AsParallel().Select(n => n * n).Sum();
        }

        private static int SquareOfSum(IEnumerable<int> nums)
        {
            var sum = nums.Sum();
            return sum * sum;
        }
    }
}
