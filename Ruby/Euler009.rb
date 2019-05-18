#!/usr/bin/env ruby

def main

  target = 1000
  for a in (3..((target - 1) / 3).ceil)
    for b in ((a + 1)..(target - a / 2).ceil)
      c = Math.sqrt(a*a + b*b)
      if c == c.floor
        c = c.to_i
        s = a + b + c

        factor, mod = target.divmod(s)
        if mod == 0
          aFinal = factor * a
          bFinal = factor * b
          cFinal = factor * c

          puts (aFinal * bFinal * cFinal)
          return
        else
          break
        end
      end
    end
  end
end

if __FILE__ == $0
  main
end
