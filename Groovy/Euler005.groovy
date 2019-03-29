#!/usr/bin/env groovy

void main() {
  factorizations = (2..20).collect { primeFactors(it) }
  Map<Integer, Integer> frequencies = [:]
  for (factorization in factorizations) {
    Map<Integer, Integer> tmpFrequencies = [:]
    for (factor in factorization) {
      if (!tmpFrequencies[factor]) {
        tmpFrequencies[factor] = 1
      } else {
        tmpFrequencies[factor]++
      }
    }
    tmpFrequencies
      .findAll { it.value > frequencies[it.key] }
      .each { key, value ->
        frequencies[key] = value
      }
  }

  Integer product = 1
  frequencies.each { factor, frequency ->
    for (_ in 1..frequency) {
      product *= factor
    }
  }
  println product
}

List<Integer> primeFactors(Integer ofInteger) {
  List<Integer> factors = []

  while (ofInteger % 2 == 0) {
    ofInteger /= 2
    factors.add(2)
  }

  for (Integer i in (3..ofInteger).by(2)) {
    if (ofInteger == 1) { break }

    while (ofInteger % i == 0) {
      ofInteger /= i
      factors.add(i)
    }
  }

  return factors
}

main()
