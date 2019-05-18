#!/usr/bin/env groovy
import java.lang.Math

class Euler013 {
  private static final String inFile = 'input/Euler013.txt'
  private static final int digits = 10

  public static void main(String[] args) {
    final Collection<Double> nums = loadFile(inFile)
    final double sum = nums.sum()

    final double exponentAdjustment = Math.ceil(Math.log10(sum)) - digits
    final double sumAdjustment = Math.pow(10, exponentAdjustment)
    final Long firstDigits = (Long)(sum / sumAdjustment)

    println firstDigits
  }

  private static Collection<Double> loadFile(String path) {
    String raw = new File(path).text
    Collection<Double> result = raw.split('\n')
      .findAll { it }
      .collect { Double.parseDouble(it) }
    return result
  }
}
