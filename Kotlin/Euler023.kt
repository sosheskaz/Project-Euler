package Euler023

import java.lang.Math
import Combinatorics.combinationsWithReplacement

fun main() {
  val target = 28123
  // println(isAbundant(12))
  val abundants = abundantNumbers().takeWhile { it <= target }.toList()

  val abundantSums = combinationsWithReplacement(abundants, 2)
    .map { it.sum() }
    .filter { it <= target }
    .distinct()

  val sumOfAbundantSums = abundantSums.sum()
  val sumOfAll = (target + 1) / 2 * target
  val sumOfNonAbundants = sumOfAll - sumOfAbundantSums
  println(sumOfNonAbundants)
}

fun abundantNumbers(): Sequence<Int> {
  return generateSequence(1){it + 1}.asSequence().filter { isAbundant(it) }.asSequence()
}

fun isAbundant(n: Int): Boolean {
  return getFactors(n).sum() > n
}

fun getFactors(n: Int): Sequence<Int> {
  val seq = sequence {
    yield(1)
    val potentialFactorSequence = generateSequence(2) { it + 1 }.takeWhile { it * it <= n }
    for (i in potentialFactorSequence) {
      if (n % i == 0) {
        yield(i)
        if (i * i != n) {
          yield(n / i)
        }
      }
    }
  }
  return seq
}
