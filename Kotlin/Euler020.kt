package Euler020

import java.math.BigInteger

fun main() {
  val target = 100
  val big0 = 0.toBigInteger()
  val big10 = 10.toBigInteger()

  var result = factorial(target)
  var sum = 0.toBigInteger()

  while (result > big0) {
    sum += result.mod(big10)
    result = result.div(big10)
  }

  println(sum)
}

fun factorial(n: Int): BigInteger {
  val product = (n downTo 1).asSequence().map { x -> x.toBigInteger() }.reduce { a, b -> a.multiply(b) }
  return product
}
