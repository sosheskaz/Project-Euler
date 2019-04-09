#!/usr/bin/env ruby

def main
  max = 20
  p = primes
    .take_while { |prime| prime <= 20 }
    .map { |prime| prime ** Math.log(max, prime).floor}
    .reduce(1, :*)
  puts p
end

def primes
  Enumerator.new do |enum|
    prime_list = []

    enum.yield 2

    for i in (3..).step(2)
      if prime_list.all? { |prime| i % prime != 0 }
        enum.yield i
        prime_list.push(i)
      end
    end
  end
end

if __FILE__ == $0
  main
end
