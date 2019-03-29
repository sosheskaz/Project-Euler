#!/usr/bin/env ruby

def main
  factorizations = (2..21).map { |n| prime_factors(n).to_a }
  frequencies = {}
  for factorization in factorizations
    tmp_frequencies = factorization.group_by { |x| x }
    tmp_frequencies.each { |factor, freq|
      freq = freq.length
      if (not frequencies.key?(factor)) or (freq > frequencies[factor])
        frequencies[factor] = freq
      end
    }
  end

  sub_products = frequencies.map { |factor, freq| factor ** freq }
  product = sub_products.reduce(:*)
  puts product
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
