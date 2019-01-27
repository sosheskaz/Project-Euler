#!/usr/bin/env swift
import Foundation

func main() {
  var sum = 0

  var previous = 1
  var current = 1
  while current < 4000000 {
    let oldPrev = previous
    previous = current
    current = previous + oldPrev

    if current % 2 == 0 {
      sum += current
    }
  }

  print(sum)
}

main()
