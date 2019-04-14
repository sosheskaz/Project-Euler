#!/usr/bin/env node
const sieve = require('./sieve.js')

function main() {
  target = 2000000;
  primes = sieve.sieve(target)
  console.log(primes.reduce((a, b) => a + b))
}

main()
