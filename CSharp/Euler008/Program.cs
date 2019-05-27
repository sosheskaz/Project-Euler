using System.Collections.Generic;
using System;
using System.Linq;

namespace Euler008
{
    class Program
    {
        private const int target = 13;

        static void Main(string[] args)
        {
            var nums = System.IO.File.ReadLines("input/Euler008.txt")
                .Where(line => !String.IsNullOrWhiteSpace(line))
                .SelectMany(line => line.Select(c => long.Parse(c.ToString())))
                .ToList();

            long biggestProduct = 0;
            var buffer = new long[target];
            for(var idx = 0; idx < nums.Count(); idx++)
            {
                buffer[idx % target] = nums[idx];
                long bufferSum = buffer.Aggregate((a, b) => a * b);
                if (bufferSum > biggestProduct)
                {
                    biggestProduct = bufferSum;
                }
            }

            Console.WriteLine(biggestProduct);
        }
    }
}
