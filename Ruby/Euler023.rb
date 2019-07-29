#!/usr/bin/env ruby

def main()
  target = 28123
  abundants = abundant_numbers()
      .take_while { |x| x <= target }
      .to_a
  abundant_sums = abundants
      .combination(2).lazy
      .map { |pair| pair.sum }
      .filter { |x| x <= target }
      .uniq
      .to_a

  abundant_sums += abundants.map { |x| x * 2 }.take_while { |x| x <= target}

  sum_of_abundants = abundant_sums.lazy.uniq.sum
  sum_of_all = (target + 1) / 2 * target
  sum_of_non_abundants = sum_of_all - sum_of_abundants

  puts sum_of_non_abundants
end

def abundant_numbers()
  Enumerator.new do |enum|
    n = 1
    while true
      if is_abundant(n)
        enum.yield(n)
      end
      n += 1
    end
  end
end

def is_abundant(n)
  return get_factors(n).sum > n
end

def get_factors(of_int)
  max = Math.sqrt(of_int).ceil

  factors = (1..max).select { |factor| of_int % factor == 0 }
      .map { |factor| [factor, of_int / factor] }
      .flatten
      .filter { |factor| factor != of_int}
      .uniq

  return factors
end

if __FILE__ == $0
  main
end
