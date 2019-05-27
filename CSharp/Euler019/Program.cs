using System.Linq;
using System;

namespace Euler019
{
    class Program
    {
        static void Main(string[] args)
        {
            var years = Enumerable.Range(1901, 100);
            var months = Enumerable.Range(1, 12).ToList();
            int sundays = years.Select(year => {
                return months
                    .Select(m => new DateTime(year, m, 1))
                    .Where(d => d.DayOfWeek == DayOfWeek.Sunday)
                    .Count();
            }).Sum();

            Console.WriteLine(sundays);
        }
    }
}
