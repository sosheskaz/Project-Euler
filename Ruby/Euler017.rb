#!/usr/bin/env ruby

def main
  target = 1000
  puts (1..target).map { |n| word_for_number(n).length }.sum
end

def word_for_number(n)
  word = ''
  if n >= 1000000
    raise "Error: Number was too big: #{n}"
  end
  if n >= 1000
    word += "#{word_for_number(n / 1000)}thousand"
    n %= 1000
  end
  if n >= 100
    word += "#{word_for_number(n / 100)}hundred"
    n %= 100
    if n != 0
      word += 'and'
    end
  end

  tens_map = {
    2 => 'twenty',
    3 => 'thirty',
    4 => 'forty',
    5 => 'fifty',
    6 => 'sixty',
    7 => 'seventy',
    8 => 'eighty',
    9 => 'ninety'
  }
  nmod10 = n / 10
  if tens_map.key?(nmod10)
    word += tens_map[nmod10]
  end
  if n >= 20
    n %= 10
  end

  ones_map = {
    0 => '',
    1 => 'one',
    2 => 'two',
    3 => 'three',
    4 => 'four',
    5 => 'five',
    6 => 'six',
    7 => 'seven',
    8 => 'eight',
    9 => 'nine',
    10 => 'ten',
    11 => 'eleven',
    12 => 'twelve',
    13 => 'thirteen',
    14 => 'fourteen',
    15 => 'fifteen',
    16 => 'sixteen',
    17 => 'seventeen',
    18 => 'eighteen',
    19 => 'nineteen'
  }
  word += ones_map[n]

  return word
end

if __FILE__ == $0
  main
end
