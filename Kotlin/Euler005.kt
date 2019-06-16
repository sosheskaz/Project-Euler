package Euler005

import java.lang.Math
import Sieve.sieve

fun main() {
  val target = 20
  val primes = Sieve.sieve(target)

  val product: Long = primes.asSequence().map { prime ->
    // ln(a) / ln(b) is equivalent to log(a) base b.
    val numer = Math.log(target.toDouble())
    val denom = Math.log(prime.toDouble())
    Math.pow(prime.toDouble(), Math.floor(numer / denom)).toLong()
  }.reduce { a, b -> a * b }

  println(product)
}
