using System.Numerics;
using System.Linq;
using System;

namespace Combinatorics
{
  public partial class Combo
  {
    public static long Factorial(long n)
    {
      long product = 1L;
      while (n > 1)
      {
        product = product * n;
        n -= 1;
      }
      return product;
    }

    public static BigInteger Factorial(BigInteger n)
    {
      BigInteger product = new BigInteger(1);
      while(n > 1)
      {
        product = product * n;
        n -= 1;
      }
      return product;
    }
  }
}
