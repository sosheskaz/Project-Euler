#!/usr/bin/env swift

import Foundation

func main() {
  // factorizations = (2..21).map { |n| prime_factors(n).to_a }
  let factorizations: [[Int]] = (2...20).map { (n: Int) -> [Int] in
    return primeFactors(of: n)
  }

  var frequencies: [Int: Int] = [:]
  for factorization in factorizations {
    let tmp_frequencies = Dictionary(grouping: factorization, by: { $0 })
    for (factor, factorArray) in tmp_frequencies {
      let freq: Int = factorArray.count
      if let oldFreq: Int = frequencies[factor] {
        if freq <= oldFreq {
          continue
        }
      }
      frequencies[factor] = freq
    }
  }

  let subProducts: [Int] = frequencies.map { Int(truncating: NSDecimalNumber(decimal: pow(Decimal($0.key), $0.value))) }
  let product: Int = subProducts.reduce(1, *)

  print(product)
}

func primeFactors(of: Int) -> [Int] {
  var num = of
  var factors: [Int] = []

  while (num % 2 == 0) {
    num /= 2
    factors.append(2)
  }

  for i in stride(from: 3, to: num+1, by: 2) {
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
