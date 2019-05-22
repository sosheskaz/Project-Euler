#!/usr/bin/env ruby

def main
  target = 1000000

  biggest_chain = -1
  biggest_num = -1
  for i in (1..target)
    chain = collatz(i)
    if chain.length > biggest_chain
      biggest_chain = chain.length
      biggest_num = i
    end
  end

  puts biggest_num
end

def collatz(n)
  result = []

  while n > 1
    result.append(n)
    if n % 2 == 0
      n /= 2
    else
      n = 3 * n + 1
    end
  end

  result.append(1)
  return result
end

if __FILE__ == $0
  main
end
