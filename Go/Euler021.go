package main

import (
	"fmt"
	"math"
)

func main() {
	const target = 10000

	properDivisorsSums := make(map[int]int)
	var amicableSum int

	for i := 1; i < target; i++ {
		// Grab the proper divisor of i
		divisorsSum, found := properDivisorsSums[i]
		if !found {
			// Cache the result for good measure
			divisorsSum = ProperDivisorsSum(i)
			properDivisorsSums[i] = divisorsSum
		}

		// Grab the proper divisors of that number
		otherDivisorsSum, found := properDivisorsSums[divisorsSum]
		if !found {
			otherDivisorsSum = ProperDivisorsSum(divisorsSum)
			properDivisorsSums[divisorsSum] = otherDivisorsSum
		}

		// Check if they're amicable (and two different numbers)
		if otherDivisorsSum == i && i != divisorsSum {
			amicableSum += i
		}
	}

	fmt.Println(amicableSum)
}

func ProperDivisorsSum(n int) int {
	sum := 1
	lim := int(math.Ceil(math.Sqrt(float64(n))))

	for i := 2; i <= lim; i++ {
		if n%i == 0 {
			sum += i
			otherDivisor := n / i
			if otherDivisor != i {
				sum += otherDivisor
			}
		}
	}

	return sum
}
