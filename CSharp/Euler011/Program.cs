using System.Collections.Generic;
using System.Linq;
using System.IO;
using System;

namespace Euler011
{
    public class Program
    {
        private const int target = 4;

        static void Main(string[] args)
        {
            List<List<long>> table = LoadFile("input/Euler011.txt");
            long biggest = -1L;

            for (int x = 0; x < table.Count; x++)
            {
                for (int y = 0; y <= table[x].Count - target; y++)
                {
                    long horiz = Enumerable.Range(0, target)
                        .Select(cursor => table[x][y + cursor])
                        .Aggregate((product, value) => product * value);

                    long vert = Enumerable.Range(0, target)
                        .Select(cursor => table[y + cursor][x])
                        .Aggregate((product, value) => product * value);

                    long diagE = -1L;
                    long diagW = -1L;

                    if (x + target < table.Count)
                    {
                        diagE = Enumerable.Range(0, target)
                            .Select(cursor => table[x + cursor][y + cursor])
                            .Aggregate((product, value) => product * value);
                    }
                    if (x - target > 0)
                    {
                        diagW = Enumerable.Range(0, target)
                            .Select(cursor => table[x - cursor][y + cursor])
                            .Aggregate((product, value) => product * value);
                    }

                    biggest = new long[5]{biggest, horiz, vert, diagE, diagW}.Max();
                }
            }

            Console.WriteLine(biggest);
        }

        public static List<List<long>> LoadFile(string path)
        {
            return File.ReadLines(path)
                .Where(line => !string.IsNullOrWhiteSpace(line))
                .Select(line => line.Split(' ').Select(item => long.Parse(item)).ToList())
                .ToList();
        }
    }
}
