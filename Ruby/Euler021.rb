#!/usr/bin/env ruby

def main
  target = 10000
  proper_divisors_sums = {}
  amicable_sum = 0

  (1..target).each { |i|
    if !proper_divisors_sums.key? i
      proper_divisors_sums[i] = get_proper_divisors_sum(i)
    end
    divisors_sum = proper_divisors_sums[i]

    if !proper_divisors_sums.key? divisors_sum
      proper_divisors_sums[divisors_sum] = get_proper_divisors_sum(divisors_sum)
    end
    other_divisors_sum = proper_divisors_sums[divisors_sum]

    if other_divisors_sum == i && i != divisors_sum
      amicable_sum += i
    end
  }
  puts amicable_sum
end

def get_proper_divisors_sum(n)
  limit = Math.sqrt(n).ceil.to_i
  nums = (2..limit).filter { |x| n % x == 0 }
  nums += nums.map { |x| n / x }
  return nums.uniq.sum + 1
end

if __FILE__ == $0
  main
end
