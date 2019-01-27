#!/usr/bin/env groovy

void main() {
  int sum = (3..999).by(3).sum()

  sum += (5..999).by(5).findAll { it % 3 != 0 }.sum()

  println sum
}

main()
