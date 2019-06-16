package Euler009

import java.lang.Math

fun main() {
  val target = 1000
  val targetDouble = target.toDouble()

  val aMax = Math.ceil((targetDouble - 2) / 3).toInt()
  for (a in 3..aMax) {
    val bMax = Math.ceil((targetDouble - a - 1) / 2).toInt()
    for (b in (a+1)..bMax) {
      val cfloat = Math.sqrt((a * a + b * b).toDouble())
      if (cfloat == Math.floor(cfloat)) {
        val c = cfloat.toInt()
        val numSum = a + b + c

        if (target % numSum == 0) {
          val factor = target / numSum
          val aFinal = factor * a
          val bFinal = factor * b
          val cFinal = factor * c

          println(aFinal * bFinal * cFinal)
          return
        } else {
          break
        }
      }
    }
  }
}
