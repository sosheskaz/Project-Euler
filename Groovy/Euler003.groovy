#!/usr/bin/env groovy

class Euler003 {
  public static void main(String[] args) {
    println primeFactors(600851475143).last()
  }

  private static List<Long> primeFactors(Long ofLong) {
    List<Long> factors = []

    while (ofLong % 2 == 0) {
      ofLong /= 2
      factors.add(2)
    }

    for (Long i in (3..ofLong).by(2)) {
      if (ofLong == 1) { break }

      while (ofLong % i == 0) {
        ofLong /= i
        factors.add(i)
      }
    }

    return factors
  }
}
