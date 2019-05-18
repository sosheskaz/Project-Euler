#!/usr/bin/env ruby

def main
  target = 4
  table = load_file 'input/Euler011.txt'
  biggest = max_product(table, target)
  puts biggest
end

def load_file(path)
  File.open(path) do |f|
    f.read.split("\n")
        .filter { |line| line }
        .map { |line| line.split(' ')
            .filter { |item| item }
            .map { |item| item.to_i }
        }
  end
end

def max_product(table, target)
  biggest = -1

  for i in (0..(table.length-1))
    for j in ((target-1)..(table[0].length-1))
      diag_east = -1
      diag_west = -1

      horz = (0..(target-1)).map { |cursor| table[i][j-cursor] }.reduce :*
      vert = (0..(target-1)).map { |cursor| table[j-cursor][i] }.reduce :*

      if i >= target
        diag_west = (0..(target-1)).map { |cursor| table[i-cursor][j-cursor] }.reduce :*
        if j <= table[0].length - target
          diag_east = (0..(target-1)).map { |cursor| table[i-cursor][j+cursor] }.reduce :*
        end
      end

      biggest = [biggest, horz, vert, diag_east, diag_west].max
    end
  end

  return biggest
end

if __FILE__ == $0
  main
end
