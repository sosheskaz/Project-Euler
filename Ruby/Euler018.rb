#!/usr/bin/env ruby
require_relative 'Euler011.rb'

def main
  puts biggest_triangle_sum('input/Euler018.txt')
end

def biggest_triangle_sum(f)
  triangle = load_file(f)

  for row in (0..triangle.length-2).reverse_each
    for col in (0..triangle[row].length-1)
      lchild = triangle[row+1][col]
      rchild = triangle[row+1][col+1]

      if lchild > rchild
        triangle[row][col] += lchild
      else
        triangle[row][col] += rchild
      end
    end
  end

  return triangle[0][0]
end

if __FILE__ == $0
  main
end
