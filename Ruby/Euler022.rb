#!/usr/bin/env ruby

BASE_LETTER_SCORE = 'a'.ord - 1

def main()
  names = load_file 'input/names.txt'
  names = names.sort
  scores = names.each_with_index.map { |n, idx| score_name(n) * (idx + 1) }
  final_score = scores.sum
  puts final_score
end

def load_file(path)
  File.open(path) do |f|
    f.read.split(',').map { |name| name.gsub(/\W/, '') }
  end
end

def score_name(name)
  return name.downcase.chars.map { |c| score_letter c }.sum
end

def score_letter(c)
  return c.ord - BASE_LETTER_SCORE
end

if __FILE__ == $0
  main
end
