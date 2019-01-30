#!/usr/bin/env swift

import Foundation

func main() {
  var biggest = -1
  for a in 100..<1000 {
    for b in a+1..<1000 {
      let product = a * b
      if product > biggest && isPalindrome(number: product) {
        biggest = product
      }
    }
  }
  print(biggest)
}

func isPalindrome(number: Int) -> Bool {
  let asString = String(number)
  return asString == String(asString.reversed())
}

main()
