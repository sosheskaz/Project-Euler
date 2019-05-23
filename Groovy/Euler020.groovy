#!/usr/bin/env groovy
import java.math.BigInteger

class Euler020 {
  private static final BigInteger target = new BigInteger(100)

  public static void main(String[] args) {
    BigInteger result = factorial(target)
    int sum = 0

    while (result > 0) {
      sum += result.mod(10)
      result = result.div(10)
    }

    println sum
  }

  private static BigInteger factorial(BigInteger n) {
    BigInteger product = new BigInteger(1)
    for (BigInteger counter = n; counter > 1; counter--) {
      product = product.multiply(counter)
    }

    return product
  }
}
