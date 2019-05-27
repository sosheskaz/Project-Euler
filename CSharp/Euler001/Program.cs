using System.Linq;
using System;

namespace Euler001
{
    class Program
    {
        private const int target = 1000;

        static void Main(string[] args)
        {
            int s = Enumerable.Range(1, target - 1)
                    .Where((i) => i % 3 == 0 || i % 5 == 0)
                    .Aggregate((sum, i) => sum + i);
            Console.WriteLine(s);
        }
    }
}
