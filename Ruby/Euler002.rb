#!/usr/bin/env ruby

def main()
  fibs = fibonacci
  evens_under_4m = fibs.take_while { |x| x < 4000000 }.filter { |x| x % 2 == 0 }
  puts evens_under_4m.sum
end

def fibonacci
  Enumerator.new do |enum|
    previous = 1
    current = 1
    enum.yield previous
    enum.yield current

    while true
      old_prev = previous
      previous = current
      current = previous + old_prev
      enum.yield current
    end
  end
end

if __FILE__ == $0
  main
end
