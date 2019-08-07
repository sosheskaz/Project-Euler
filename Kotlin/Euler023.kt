package Euler023

import Combinatorics.combinationsWithReplacement

fun main() {
  val target = 28123
  val abundants = abundantNumbers().takeWhile { target >= it }.toList()

  val abundantSums = combinationsWithReplacement(abundants, 2)
    .map { it.sum() }
    .filter { target >= it }
    .distinct()

  // .sum() collapses the generator, so it eats a lot of memory because Java
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
    val potentialFactorSequence = generateSequence(2) { it + 1 }.takeWhile { n >= it * it }
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
