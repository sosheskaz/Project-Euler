#!/usr/bin/env groovy
import java.lang.Math

void main() {
  final int target = 1000

	for (int a = 3; a*3+2 <= target; a++) {
		for (int b = a + 1; a+2*b+1 <= target; b++) {
			double cfloat = Math.sqrt((double)(a * a + b * b))
			if (cfloat == Math.floor(cfloat)) {
				int c = (int) cfloat
				int sum = a + b + c

				if (target % sum == 0) {
					// We have a match.
					int factor = target / sum
					int aFinal = factor * a
					int bFinal = factor * b
					int cFinal = factor * c

					println (aFinal * bFinal * cFinal)
					return
				} else {
					break
				}
			}
		}
	}
}

main()
