using System.Linq;
using System.Collections.Generic;
using System;

namespace Euler004
{
    class Program
    {
        static void Main(string[] args)
        {
            int biggest = -1;

            foreach (int a in Enumerable.Range(100, 900)) {
                foreach(int b in Enumerable.Range(100, 900)) {
                    int product = a * b;
                    String productString = product.ToString();
                    if (product > biggest && productString == new String(productString.Reverse().ToArray()))
                    {
                        biggest = product;
                    }
                }
            }

            Console.WriteLine(biggest);
        }
    }
}
