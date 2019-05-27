using System.Numerics;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using System;


// def main():
//     digits = 10
//     infile = 'input/Euler013.txt'

//     nums = parse_file(infile)
//     numsum = sum(nums)

//     print(str(numsum)[:digits])


// def parse_file(path) -> list:
//     with open(path) as f:
//         return [int(num) for num in f.readlines()]

namespace Euler013
{
    class Program
    {
        private const int digits = 10;

        static void Main(string[] args)
        {
            var nums = ParseFile("input/Euler013.txt");
            var numSum = nums.Aggregate((a, b) => a + b);
            Console.WriteLine(numSum.ToString().Substring(0, digits));
        }

        static IEnumerable<BigInteger> ParseFile(string path)
        {
            return File.ReadLines(path).AsParallel().Select(line => BigInteger.Parse(line));
        }
    }
}
