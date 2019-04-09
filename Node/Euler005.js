#!/usr/bin/env node
const generators = require("./generators.js")


function main() {
  const max = 20

  // avoid callback hell 🔥
  var walker = primes()
  walker = generators.takeWhile(walker, (prime) => { return prime < max; });
  walker = generators.map(walker, (prime) => {
    // ln(a) / ln(b) is equivalent to log(a) base b.
    let numer = Math.log(max);
    let denom = Math.log(prime);
    let subProduct = Math.pow(prime, Math.floor(numer / denom));
    return subProduct;
  })
  let product = generators.reduce(walker, 1, (accumulator, item) => { return accumulator * item; })

  console.log(product)
}

// Array has map, but generators don't.
function* map(fn, xs) {
  for (let x of xs) {
    yield fn(x);
  }
}

function* primes() {
  primeList = []

  yield 2;

  for (let i = 3; true; i += 2) {
    if (primeList.every((prime) => { return i % prime != 0})) {
      yield i;
      primeList.push(i);
    }
  }
}

main()
