using System;
using System.Linq;
using System.Collections.Generic;

namespace Euler022
{
    class Program
    {
        static void Main(string[] args)
        {
            var names = LoadFile("input/names.txt").ToList();
            names.Sort();

            var score = names.Select((name, index) => (index + 1) * ScoreName(name)).Sum();

            Console.WriteLine(score);
        }

        static int ScoreName(string name)
        {
            var chars = name.ToLower().ToCharArray();
            var score = 0;

            foreach (var c in chars) {
                score += ScoreChar(c);
            }

            return score;
        }

        static int ScoreChar(char c)
        {
            return (int)(c - 'a' + 1);
        }


        public static IEnumerable<string> LoadFile(string path)
        {
            char[] trim = {'"'};
            return System.IO.File.ReadAllLines(path)[0].Split(",").Select((name) => name.Trim(trim));
        }
    }
}
