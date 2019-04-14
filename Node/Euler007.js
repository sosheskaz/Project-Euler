#!/usr/bin/env node
const sieve = require('./sieve.js')

function main() {
  const target = 10001;
  let primes = sieve.sieve(200000);
  console.log(primes[target])
}

main()
