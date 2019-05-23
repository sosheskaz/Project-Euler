#!/usr/bin/env ruby

require_relative 'Euler015.rb'

def main
  target = 100
  result = factorial(target)
  sum = 0

  while result > 0
    result, digit = result.divmod(10)
    sum += digit
  end

  puts sum
end

if __FILE__ == $0
  main
end
