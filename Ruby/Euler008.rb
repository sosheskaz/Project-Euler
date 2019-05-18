#!/usr/bin/env ruby

def main
  factor_ct = 13
  ord0 = '0'.ord

  contents = File.open('input/Euler008.txt') do |f|
    f.read.split('').filter { |c| '0' <= c && c <= '9' }.map { |c| c.ord - ord0 }
  end

  buffer = factor_ct.times.map { 0 }
  product = 0

  contents.each_with_index { |val, idx|
    buffer[idx % factor_ct] = val
    product = [product, buffer.reduce(1, :*)].max
  }

  puts product
end

if __FILE__ == $0
  main
end
