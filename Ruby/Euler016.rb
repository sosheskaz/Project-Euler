#!/usr/bin/env ruby

def main
  target = 1000

  x = 2 ** target
  sum = 0

  while x > 0
    x, mod = x.divmod(10)
    sum += mod
  end

  puts sum
end

if __FILE__ == $0
  main
end
