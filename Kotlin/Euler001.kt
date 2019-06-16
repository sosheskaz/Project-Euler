package Euler001

fun main(args: Array<String>) {
  val target = 1000
  val limit = target - 1
  var sum: Int = 0

  for (i in 3..limit step 3) {
    sum += i
  }

  for (i in 5..limit step 5) {
    if (i % 3 != 0) {
      sum += i
    }
  }

  println(sum)
}
