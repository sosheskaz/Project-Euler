#!/usr/bin/env groovy
import java.math.BigInteger

class Euler016 {
  private static final int target = 1000

  private static final BigInteger bigZero = new BigInteger(2)

  public static void main(String[] args) {
    BigInteger x = new BigInteger(2)
    x = x.power(target)

    int sum = 0
    while (x > 0) {
      int digit = x.mod(10)
      sum += digit
      x = x.div(10)
    }

    println sum
  }
}
