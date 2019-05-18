#!/usr/bin/env groovy
import java.lang.Math

class Euler012 {
  public static void main(String[] args) {
    final int target = 500

    int triangle = 0

    for (int incrementer = 1; ; incrementer++) {
      triangle += incrementer
      Collection<Integer> factors = Euler012.getFactors triangle
      if (factors.size() >= target) {
        println triangle
        break
      }
    }
  }

  private static Collection<Integer> getFactors(int ofInt) {
    HashSet factors = []

    int max = (int)Math.ceil(Math.sqrt((double)ofInt))
    for (int f = 1; f <= max; f++) {
      if (ofInt % f != 0) {
        continue
      }

      factors.add(f)
      factors.add(ofInt / f)
    }

    return factors
  }
}
