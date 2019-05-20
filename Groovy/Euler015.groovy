#!/usr/bin/env groovy
import java.lang.Math

class Euler015 {
  private static final Long target = 20

  public static void main(String[] args) {
    println combinatoric(target * 2, target)
  }

  private static Long combinatoric(Long n, Long r) {
    double numer = factorial(n)
    double denom = factorial(r) * factorial(n - r)
    return (Long)(Math.round(numer / denom))
  }

  private static double factorial(Long n) {
    double p = 1.0
    for (Long x = n; x > 1; x--) {
      p *= (double) x
    }
    return p
  }
}
