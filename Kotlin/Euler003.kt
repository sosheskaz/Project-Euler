package Euler003

fun main() {
  val target = 600851475143
  println(primeFactors(target).last())
}

fun primeFactors(of: Long): List<Long> {
  var factors = mutableListOf<Long>()
  var n = of

  while (n % 2L == 0L) {
    n /= 2L
    factors.add(2L)
  }

  for (i in 3..n step 2) {
      if (n == 1L) { break }

      while (n % i == 0L) {
        n /= i
        factors.add(i)
      }
    }

  return factors
}
