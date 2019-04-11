import groovy.transform.CompileStatic
import java.lang.Math

def sieve(Integer limit) {
  boolean[] sieve = new boolean[limit + 1]

  Integer x2, y2, n, nMod12

  Integer sqrtLimit = (int)Math.sqrt(limit)
  for (Integer x = 1; x <= sqrtLimit; x += 1) {
    x2 = x * x
    for (Integer y = 1; y <= sqrtLimit; y += 1) {
      y2 = y * y

      n = 4 * x2 + y2
      nMod12 = n % 12
      if (n <= limit && (nMod12 == 1 || nMod12 == 5)) {
        sieve[n] ^= true
      }

      n = 3 * x2 + y2
      if (n <= limit && n % 12 == 7) {
        sieve[n] ^= true
      }

      n = 3 * x2 - y2
      if (n <= limit && x2 > y2 && n % 12 == 11) {
        sieve[n] ^= true
      }
    }
  }

  Integer r2;
  for (Integer r = 5; r <= sqrtLimit; r++) {
    if (sieve[r]) {
      r2 = r * r;
      for (Integer s = r2; s <= limit; s += r2) {
        sieve[s] = false;
      }
    }
  }

  List<Integer> primes = new ArrayList<>();

  if (limit >= 2) {
    primes.add(2);
  }
  if (limit >= 3) {
    primes.add(3);
  }

  for (Integer i = 5; i <= limit; i += 2) {
    if (sieve[i]) {
      primes.add(i);
    }
  }

  return primes;
}

return this
