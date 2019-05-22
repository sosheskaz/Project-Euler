#!/usr/bin/env ruby

def main
  target = 20
  puts combinatoric(target * 2, target)
end

def combinatoric(n, r)
  numer = factorial(n)
  denom = factorial(r) * factorial(n - r)
  return numer / denom
end

def factorial(n)
  p = 1
  while n > 1
    p *= n
    n -= 1
  end
  return p
end

if __FILE__ == $0
  main
end
