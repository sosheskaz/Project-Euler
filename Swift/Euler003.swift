#!/usr/bin/env swift

import Foundation

func main() {
  print(primeFactors(of: 600851475143).last!)
}

func primeFactors(of: Int) -> [Int] {
  var num = of
  var factors: [Int] = []

  while (num % 2 == 0) {
    num /= 2
    factors.append(2)
  }

  for i in stride(from: 3, to: num, by: 2) {
    if (num == 1) {
      break
    }

    while (num % i == 0) {
      num /= i
      factors.append(i)
    }
  }

  return factors
}

main()
