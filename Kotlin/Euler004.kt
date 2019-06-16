package Euler004

fun main() {
  val target = 1000
  val lim = target - 1

  var biggest = -1

  for (a in 100..lim) {
    for (b in (a+1)..lim) {
      val product = a * b

      if (product > biggest && isPalindrome(product)) {
        biggest = product
      }
    }
  }

  println(biggest)
}

fun isPalindrome(n: Int): Boolean {
  val asString = n.toString()
  return asString == asString.reversed()
}
