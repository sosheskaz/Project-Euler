using System.Linq;
using System;

namespace Euler009
{
    class Program
    {
        private const int target = 1000;

        static void Main(string[] args)
        {
            foreach(int a in Enumerable.Range(3, (target - 1) / 3 - 2))
            {
                foreach(int b in Enumerable.Range(a + 1, target - a / 2 - a - 1))
                {
                    double c = Math.Sqrt(a * a + b * b);
                    if (c == Math.Floor(c))
                    {
                        int cInt = (int) c;
                        int s = a + b + cInt;

                        int factor = target / s;
                        int mod = target % s;
                        if (mod == 0)
                        {
                            Console.WriteLine(factor * factor * factor * a * b * cInt);
                            return;
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
    }
}
