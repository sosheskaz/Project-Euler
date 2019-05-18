#!/usr/bin/env ruby

def main
  target = 500
  triangle = 0
  incrementer = 1
  while true
    triangle += incrementer
    if get_factors(triangle).length >= target
      puts triangle
      break
    end
    incrementer += 1
  end
end

def get_factors(of_int)
  max = Math.sqrt(of_int).ceil

  factors = (1..max).select { |factor| of_int % factor == 0 }
      .map { |factor| [factor, of_int / factor] }
      .flatten
      .uniq

  return factors
end

if __FILE__ == $0
  main
end
