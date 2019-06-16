package Euler014

fun main() {
  val target = 1000000L

  val chains = (0L..target).asSequence().map { i -> collatz(i) }

  var biggestChain = -1L
  var biggestStarting = -1L

  for (chain in chains) {
    val l = chain.size.toLong()
    if (l > biggestChain) {
      biggestChain = l
      biggestStarting = chain[0]
    }
  }

  println(biggestStarting)
}

fun collatz(n: Long): List<Long> {
  var output: MutableList<Long> = mutableListOf()
  var counter = n
  while (counter > 1L) {
    output.add(counter)
    if (counter % 2L == 0L) {
      counter /= 2L
    } else {
      counter = 3L * counter + 1L
    }
  }
  output.add(counter)

  return output
}
