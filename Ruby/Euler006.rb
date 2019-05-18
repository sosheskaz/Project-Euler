#!/usr/bin/env ruby

def main
  n = 100
  sum_of_squares = (1..n).map { |x| x ** 2 }.sum
  square_of_sums = (1..n).sum ** 2
  puts square_of_sums - sum_of_squares
end

if __FILE__ == $0
  main
end
