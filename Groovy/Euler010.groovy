#!/usr/bin/env groovy
import groovy.transform.SourceURI
import java.nio.file.Path
import java.nio.file.Paths

@SourceURI
URI sourceUri

Path scriptLocation = Paths.get(sourceUri)
sieve = evaluate(new File("${scriptLocation.parent}/lib/sieve.groovy"))

void main() {
  final int target = 2000000
  List<Integer> primes = sieve.sieve(2000000)

  // We can't use vanilla sum() becuase of integer overflow.
  Long sum = primes.inject({ a, b -> (Long)a + b })
  println sum
}

main()
