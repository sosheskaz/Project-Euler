#!/usr/bin/env node

function sieve(limit) {
  var sieve = Array(limit + 1);
  sieve.fill(false);
  var sqrtlim = Math.ceil(Math.sqrt(limit));

  for (let x = 1; x <= sqrtlim; x++) {
    var x2 = x * x;
    for (let y = 1; y <= sqrtlim; y++) {
      var y2 = y * y;

      let n = 4 * x2 + y2;
      let nmod12 = n % 12;
      if (n <= limit && (nmod12 == 1 || nmod12 == 5)) {
        sieve[n] = !sieve[n];
      }

      n = 3 * x2 + y2;
      if (n <= limit && n % 12 == 7) {
        sieve[n] = !sieve[n];
      }

      n = 3 * x2 - y2;
      if (n <= limit && x2 > y2 && n % 12 == 11) {
        sieve[n] = !sieve[n];
      }
    }
  }

  for (let r = 5; r <= sqrtlim; r += 2) {
    if (r < sieve.length && sieve[r]) {
      let s = r * r;
      for (let k = s; k <= limit; k += s) {
        sieve[k] = false
      }
    }
  }

  sieve[2] = true
  sieve[3] = true

  var primes = []
  sieve.forEach((isPrime, value) => {
    if (isPrime) {
      primes.push(value)
    }
  })

  return primes
}
exports.sieve = sieve
