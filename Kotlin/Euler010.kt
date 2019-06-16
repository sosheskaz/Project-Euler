package Euler010

import Sieve.sieve

fun main() {
  val target = 2000000
  val primes = Sieve.sieve(target)
  val sum = primes.asSequence().map { p -> p.toLong() }.sum()
  println(sum)
}
