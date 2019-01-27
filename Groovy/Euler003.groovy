#!/usr/bin/env groovy

void main() {
  println primeFactors(600851475143).last()
}

List<Long> primeFactors(Long ofLong) {
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

main()
