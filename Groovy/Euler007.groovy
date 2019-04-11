#!/usr/bin/env groovy
import groovy.transform.SourceURI
import java.nio.file.Path
import java.nio.file.Paths

@SourceURI
URI sourceUri

Path scriptLocation = Paths.get(sourceUri)

sieve = evaluate(new File("${scriptLocation.parent}/lib/sieve.groovy"))

void main() {
  println sieve.sieve(200000)[10001]
}

main()
