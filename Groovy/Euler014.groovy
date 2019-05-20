#!/usr/bin/env groovy

class Euler014 {
  private static final Long target = 1000000

  public static void main(String[] args) {

    def chains = (0L..target).stream()
        .map { i -> [num: i, collatz: collatz(i)] }
        // .max { it.collatz.size() }

    int biggestChain = -1
    int biggestStarting = -1
    for (def chain in chains) {
      int l = chain.collatz.size()
      if (l > biggestChain) {
        biggestChain = l
        biggestStarting = chain.num
      }
    }

    println biggestStarting
  }


  private static List<Long> collatz(Long n) {
    List<Long> output = []
    while (n > 1) {
      output.add(n)
      if (n % 2 == 0) {
        n /= 2
      } else {
        n = 3 * n + 1
      }
    }
    output.add(n)

    return output
  }
}
