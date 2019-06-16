package Euler016

// import java.math.BigInteg

fun main() {
  val target = 1000
  val big0 = 0.toBigInteger()
  val big10 = 10.toBigInteger()

  var x = 2.toBigInteger()
  x = x.pow(target)

  var sum = big0
  while (x > big0) {
    val digit = x.mod(big10)
    sum += digit
    x = x.div(big10)
  }

  println(sum)
}
