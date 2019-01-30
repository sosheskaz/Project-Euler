#!/usr/bin/env ruby

def main
  combos = (100..999).to_a.combination(2)
  products = combos.map { |x, y| x * y }
  palindromes = products.filter { |x| x.to_s == x.to_s.reverse }
  biggest = palindromes.max
  puts biggest
end

if __FILE__ == $0
  main
end
