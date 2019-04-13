#!/usr/bin/env ruby
require 'set'

def sieve(lim)
  sieve = lim.times.collect { |_| false }
  sqrtlim = Math.sqrt(lim).ceil.to_i

  part1Mods = [1, 5].to_set

  r = (1..sqrtlim).map { |a| a * a }
  for (x2, y2) in r.product(r)
    n = 4 * x2 + y2
    if n <= lim && (part1Mods.include? (n % 12))
      sieve[n] ^= true
    end

    n = 3 * x2 + y2
    if n <= lim && n % 12 == 7
      sieve[n] ^= true
    end

    n = 3 * x2 - y2
    if n <= lim && x2 > y2 && n % 12 == 11
      sieve[n] ^= true
    end
  end

  for r in (5..sqrtlim)
    s = r * r
    for k in (s..lim).step(s)
      sieve[k] = false
    end
  end

  sieve[2] = true
  sieve[3] = true

  return sieve.each_with_index.filter { |b, i| b }.map { |b, i| i }
end

if __FILE__ == $0
  puts sieve(30)
end
