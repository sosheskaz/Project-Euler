using System.Linq;
using System.Collections.Generic;
using System;

namespace Euler018
{
    class Program
    {
        static void Main(string[] args)
        {
            var triangle = Euler011.Program.LoadFile("input/Euler018.txt");
            Console.WriteLine(GetBiggestTriangleSum(triangle));
        }


        static long GetBiggestTriangleSum(List<List<long>> triangle)
        {
            for (int row = triangle.Count - 2; row >= 0; row--)
            {
                foreach(int col in Enumerable.Range(0, triangle[row].Count))
                {
                    long lChild = triangle[row + 1][col];
                    long rChild = triangle[row + 1][col + 1];

                    if (lChild > rChild)
                    {
                        triangle[row][col] += lChild;
                    }
                    else
                    {
                        triangle[row][col] += rChild;
                    }
                }
            }

            return triangle[0][0];
        }
    // def get_biggest_triangle_sum(of_file):
    // triangle = Euler011.load_file(of_file)

    // for row in reversed(range(0, len(triangle) - 1)):
    //     for col in range(0, len(triangle[row])) :
    //         lchild = triangle[row + 1][col]
    //         rchild = triangle[row + 1][col + 1]

    //         if lchild > rchild:
    //             triangle[row][col] += lchild
    //         else:
    //             triangle[row][col] += rchild

    // return triangle[0][0]
    }
}
