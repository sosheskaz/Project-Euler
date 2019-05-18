#!/usr/bin/env ruby
require_relative 'sieve.rb'

def main
  puts sieve(200000)[10001]
end

if __FILE__ == $0
  main
end
