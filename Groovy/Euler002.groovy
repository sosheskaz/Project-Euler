#!/usr/bin/env groovy

void main() {
  int sum = 0

  int previous = 1
  int current = 1
  while (current < 4000000) {
    oldPrev = previous
    previous = current
    current = previous + oldPrev

    if (current % 2 == 0) {
      sum += current
    }
  }

  println sum
}

main()
