#!/usr/bin/env swift
import Foundation

func main() {
  var sum: Int = stride(from: 3, to: 1000, by: 3).reduce(0, +)

  sum += stride(from: 5, to: 1000, by: 5).filter { x in x % 3 != 0 }.reduce(0, +)

  print(sum)
}

main()
