using System.Collections.ObjectModel;
using System.Linq;
using System.Collections.Generic;
using System;

namespace Euler012
{
    class Program
    {
        private const int target = 500;

        static void Main(string[] args)
        {
            var triangles = TriangleNumbers();
            var result = triangles
                .Select(t => (t, GetFactors(t)))
                .SkipWhile(tup => tup.Item2.Count < target)
                .First();
            Console.WriteLine(result.Item1);
        }

        static HashSet<int> GetFactors(int n)
        {
            return Enumerable.Range(1, int.MaxValue)
                .TakeWhile(f => f * f <= n)
                .Where(f => n % f == 0 )
                .SelectMany(f => new int[2]{f, n / f})
                .ToHashSet();
        }

        static IEnumerable<int> TriangleNumbers()
        {
            int i = 0;
            int incrementer = 1;
            while (true)
            {
                i += incrementer++;
                yield return i;
            }
        }
    }
}
