#!/usr/bin/env ruby

def main
  target = 1000000
  digits = (0..9).to_a
  perms = digits.permutation.lazy
  result = perms.drop(target - 1).first
  puts result.join("")
end

if __FILE__ == $0
  main
end
