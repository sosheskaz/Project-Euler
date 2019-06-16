package Euler015

fun main() {
  val target = 20L

  println(combinatoric(target * 2, target))
}

fun combinatoric(n: Long, r: Long): Long {
  val numer = factorial(n)
  val denom = factorial(r) * factorial(n - r)
  return Math.round(numer / denom).toLong()
}

fun factorial(n: Long): Double {
  return (n downTo 2).asSequence().map { x -> x.toDouble() }.reduce { a, b -> a * b }
}
