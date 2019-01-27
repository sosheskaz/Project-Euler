#!/usr/bin/env ruby

def main
  sum = (3..999).step(3).sum { |x| x }

  sum += (5..999).step(5).filter { |x| x % 3 != 0 }.sum

  puts sum
end

if __FILE__ == $0
  main
end
