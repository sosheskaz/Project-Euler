#!/usr/bin/env groovy
import java.lang.Math

class Euler008 {
  public static void main(String[] args) {
    final int factorCt = 13
    final byte char0 = 48
    final byte char9 = 57
    Long[] buffer = new int[factorCt]
    Long product = 0

    Long[] fileContents = new File('input/Euler008.txt').text
    fileContents = fileContents
      .findAll { it >= char0 && it <= char9 }
      .collect { it - char0 }

    fileContents.eachWithIndex { Long digit, int index ->
      buffer[index % factorCt] = digit

      product = Math.max(product, buffer.inject(1L, { collector, x -> collector * x}))
    }

    println product
  }
}
