package Euler006

fun main() {
  val n = 100L
  val sumOfSquares = (1L..n).asSequence().map { it -> it * it }.sum()
  val sum = (1L..n).sum()
  val squareOfSum = sum * sum
  println(squareOfSum - sumOfSquares)
}
