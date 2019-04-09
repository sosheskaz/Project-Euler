#!/usr/bin/env groovy

void main() {
  final Long n = 100L
  final Long sumOfSquares = (1L..n).collect { it * it }.inject(0, { a, b -> a + b })
  final Long sum = (1L..n).sum()
  final Long squareOfSum = sum * sum
  println squareOfSum - sumOfSquares
}

main()
