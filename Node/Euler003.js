#!/usr/bin/env node

function main() {
  factors = Array.from(primeFactors(600851475143))
  console.log(factors[factors.length-1])
}

function* primeFactors(num) {
  var factors = [];

  while (num % 2 == 0) {
    num /= 2;
    yield 2;
  }

  for (let i = 3; i <= num; i += 2) {
    if (num == 1) {
      break;
    }

    while (num % i == 0) {
      num /= i
      yield i;
    }
  }
}

if (require.main === module) {
  main();
}
