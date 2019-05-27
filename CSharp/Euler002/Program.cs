using System;

namespace Euler002
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;

            int previous = 1;
            int current = 1;
            while (current < 4000000)
            {
                int oldPrev = previous;
                previous = current;
                current = previous + oldPrev;

                if (current % 2 == 0) {
                    sum += current;
                }
            }

            Console.WriteLine(sum);
        }
    }
}
