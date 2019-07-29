using System;
using System.Linq;
using System.Collections.Generic;
using Combinatorics;

namespace Euler022
{
  class Program
  {
    private const int target = 28123;

    static void Main(string[] args)
    {
      var abundants = AbundantNumbers().TakeWhile((x) => x <= target).ToList();
      var abundantSums = Combo.GetCombinationsWithReplacement(abundants, 2).AsParallel()
          .Select(pair => pair.Sum())
          .Where(s => s <= target)
          .Distinct();
      var sumOfAbundantSums = abundantSums.Sum();

      var sumOfAll = (target + 1) / 2 * target;
      var sumOfNonAbundantSums = sumOfAll - sumOfAbundantSums;

      Console.WriteLine(sumOfNonAbundantSums);
    }

    static IEnumerable<int> AbundantNumbers() {
      return from x in Enumerable.Range(1, int.MaxValue) where IsAbundant(x) select x;
    }

    static bool IsAbundant(int n) {
      return GetFactors(n).Sum() > n;
    }

    static IEnumerable<int> GetFactors(int n) {
      var limit = Convert.ToInt32(Math.Floor(Math.Sqrt(n))) + 1;
      yield return 1;

      foreach (var i in Enumerable.Range(2, limit - 2)) {
        if (n % i == 0) {
          yield return i;
          if (i * i != n)
            yield return n / i;
        }
      }
    }
  }
}
