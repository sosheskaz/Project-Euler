#!/usr/bin/env ruby
require_relative 'sieve.rb'

def main
  target = 2000000
  primes = sieve(target)
  puts primes.sum
end

if __FILE__ == $0
  main
end
