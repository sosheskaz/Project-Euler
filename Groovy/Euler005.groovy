#!/usr/bin/env groovy

class Euler005 {
  public static void main(String[] args) {
    final Long max = 20
    final Double maxFloat = (Double) max

    List<Long> primeList = primes(max)

    Long product = primeList.collect { prime ->
      // ln(a) / ln(b) is equivalent to log(a) base b.
      double numer = Math.log(maxFloat)
      double denom = Math.log(prime)
      return (int) Math.pow(prime, Math.floor(numer / denom))
    }.inject(1, { result, i -> result * i })

    println product
  }

  private static List<Long> primes(Long upTo) {
    List<Long> primeList = []
    if (upTo < 2) {
      return primeList
    }

    primeList.add(2)

    for (Long i in (3..upTo).by(2)) {
      if (!primeList.any { i % it == 0 }) {
        primeList.add(i)
      }
    }

    return primeList
  }
}
