#!/usr/bin/env node
const generators = require("./generators.js");
const combinatorics = require("./combinatorics.js");

function main() {
  const target = 28123;

  var abundants = generators.takeWhile(abundantNumbers(), (x) => x <= target);
  abundants = Array.from(abundants);
  var abundantSums = combinatorics.combinationsWithReplacement(abundants, 2);
  abundantSums = generators.map(abundantSums, (pair) => pair.reduce((a, b) => a + b));
  abundantSums = generators.filter(abundantSums, (x) => x <= target);
  abundantSums = new Set(abundantSums);

  var sumOfAbundantSums = generators.reduce(abundantSums, 0, (a, b) => a + b);
  var sumOfAll = (target + 1) / 2 * target;
  var sumOfNonAbundants = sumOfAll - sumOfAbundantSums;
  console.log(sumOfNonAbundants);
}

function* abundantNumbers() {
  var n = 1;
  while (true) {
    if (isAbundant(n)) {
      yield n;
    }
    n++;
  }
}

function isAbundant(n) {
  return generators.reduce(getFactors(n), 0, (a, b) => a + b) > n;
}

function* getFactors(n) {
  var limit = Math.floor(Math.sqrt(n)) + 1;
  yield 1;
  for (let i = 2; i < limit; i++) {
    if (n % i == 0) {
      yield i;
      if (i * i != n)
        yield n / i;
    }
  }
}

if (require.main == module) {
  main()
}
