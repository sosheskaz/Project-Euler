#!/usr/bin/env ruby

def main
    puts prime_factors(600851475143).to_a.last
end

def prime_factors(of_number)
  Enumerator.new do |enum|
    while of_number % 2 == 0
      of_number /= 2
      enum.yield 2
    end

    for i in (3..of_number).step(2)
      if of_number == 1
        break
      end

      while of_number % i == 0
        of_number /= i
        enum.yield i
      end
    end
  end
end

if __FILE__ == $0
  main
end
