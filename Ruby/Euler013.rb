#!/usr/bin/env ruby

def main
  path = 'input/Euler013.txt'
  digits = 10

  nums = parse_file(path)

  sum = nums.sum

  puts sum.to_s.slice(0, 10)
end

def parse_file(path)
  File.open(path) do |f|
    f.read.split("\n")
        .filter { |line| line }
        .map { |line| line.to_i }
  end
end

if __FILE__ == $0
  main
end
