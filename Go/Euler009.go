package main

import (
	"fmt"
	"math"
	"os"
)

func main() {
	const target = 1000

	// Multiplying any triangle times an integer yields another triangle.
	// 9 + 16 = 25 -> [3, 4, 5] • 2 = [6, 8, 10] -> 36 + 64 = 100
	// This could be further optimized by starting with a smaller search space and expanding out.

	for a := 3; a*3+2 <= target; a++ {
		for b := a + 1; a+2*b+1 <= target; b++ {
			cfloat := math.Sqrt(float64(a*a + b*b))
			if cfloat == math.Floor(cfloat) {
				c := int(cfloat)
				sum := a + b + c

				if target%sum == 0 {
					// We have a match.
					factor := target / sum
					aFinal := factor * a
					bFinal := factor * b
					cFinal := factor * c

					fmt.Println(aFinal * bFinal * cFinal)
					os.Exit(0)
				} else {
					break
				}
			}
		}
	}
}
