#!/usr/bin/env ruby
require 'date'

def main
  sunday = 7
  sundays = 0

  for year in (1901..2000)
    for month in (1..12)
      d = Date.new(year, month, 1)
      if d.cwday == 7
        sundays += 1
      end
    end
  end

  puts sundays
end

if __FILE__ == $0
  main
end
