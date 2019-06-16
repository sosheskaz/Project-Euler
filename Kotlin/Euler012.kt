package Euler012

import java.lang.Math

fun main() {
  val target = 500

  var triangle = 0

  var incrementer = 1
  while (true) {
    triangle += incrementer++
    val factors = getFactors(triangle)
    if (factors.size >= target) {
      println(triangle)
      break
    }
  }
}

fun getFactors(n: Int): Set<Int> {
  var factors: MutableSet<Int> = mutableSetOf()

  val max = Math.sqrt(n.toDouble()).toInt()
  for (f in 1..max) {
    if (n % f != 0) continue

    factors.add(f)
    factors.add(n / f)
  }

  return factors
}
