package Sieve

import java.lang.Math

fun sieve(limit: Int): List<Int> {
  val limitLong = limit.toLong()
  var sieve = BooleanArray(limit + 1, { false })

  val sqrtLimit = Math.ceil(Math.sqrt(limit.toDouble())).toLong()

  for (x in 1L..sqrtLimit) {
    val x2 = x * x
    for (y in 1L..sqrtLimit) {
      val y2 = y * y

      var n: Long = 4L * x2 + y2
      val nMod12: Long = n % 12L
      if (n <= limitLong && (nMod12 == 1L || nMod12 == 5L)) {
        sieve[n.toInt()] = !sieve[n.toInt()]
      }

      n = 3L * x2 + y2
      if ( n <= limitLong && n % 12L == 7L) {
        sieve[n.toInt()] = !sieve[n.toInt()]
      }

      n = 3L * x2 - y2
      if (n <= limit && x2 > y2 && n % 12L == 11L) {
        sieve[n.toInt()] = !sieve[n.toInt()]
      }
    }
  }

  for (r in 5..sqrtLimit.toInt()) {
    if (sieve[r]) {
      val r2 = r * r
      for (s in r2..limit step r2) {
        sieve[s] = false
      }
    }
  }

  sieve[2] = true
  sieve[3] = true

  val primes = sieve.asSequence().withIndex().filter { item -> item.value }.map { item -> item.index }

  return primes.toList()
}
