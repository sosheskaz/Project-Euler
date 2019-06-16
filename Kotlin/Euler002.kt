package Euler002

fun main() {
  val target = 4000000

  var sum = 0
  var previous = 1
  var current = 1

  while (current < target) {
    val oldPrev = previous
    previous = current
    current = previous + oldPrev

    if (current % 2 == 0) {
      sum += current
    }
  }

  println(sum)
}
