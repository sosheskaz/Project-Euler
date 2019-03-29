#!/usr/bin/env node

function main() {
  var frequencies = {}
  for (let i = 2; i <= 20; i++) {
    var tmpFrequencies = {}
    for (let factor of primeFactors(i)) {
      if (!tmpFrequencies[factor]) {
        tmpFrequencies[factor] = 1;
      } else {
        tmpFrequencies[factor]++;
      }
    }

    Object.keys(tmpFrequencies)
      .filter((key) => {
        return frequencies[key] === undefined || tmpFrequencies[key] > frequencies[key]
      })
      .forEach((key) => {
        return frequencies[key] = tmpFrequencies[key]
      });
  }

  var product = 1
  Object.keys(frequencies).forEach(function(factor) {
    for (let i = 0; i < frequencies[factor]; i++) {
      product *= factor;
    }
  })
  console.log(product);
}

function* primeFactors(num) {
  while (num % 2 == 0) {
    yield 2;
    num /= 2;
  }

  for (let i = 3; i <= num; i += 2) {
    if (num == 1) {
      break;
    }

    while (num % i == 0) {
      num /= i;
      yield i;
    }
  }
}

main()
