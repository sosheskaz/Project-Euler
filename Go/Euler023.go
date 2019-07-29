package main

import (
	"fmt"
	"os"
)

func main() {
	const target = 28123
	// fmt.Println(isAbundant(12))
	abundants := abundantNumbers(target)
	abundantPairs, err := CombinationsWithReplacement(*abundants, 2)
	if err != nil {
		fmt.Println(fmt.Errorf("Error: %+v", err))
		os.Exit(1)
	}

	abundantSums := make(chan int)
	go func() {
		defer close(abundantSums)

		for pair := range abundantPairs {
			s := pair[0] + pair[1]
			if s <= target {
				abundantSums <- s
			}
		}
	}()

	uniqueAbundantSums := make(map[int]bool)

	for subSum := range abundantSums {
		uniqueAbundantSums[subSum] = true
	}

	sumOfAbundantSums := 0
	for val, _ := range uniqueAbundantSums {
		sumOfAbundantSums += val
	}

	sumOfAll := (target + 1) / 2 * target
	sumOfNonAbundantSums := sumOfAll - sumOfAbundantSums

	fmt.Println(sumOfNonAbundantSums)
}

func abundantNumbers(upTo int) *[]int {
	var abundants []int

	for i := 1; i <= upTo; i++ {
		if isAbundant(i) {
			abundants = append(abundants, i)
		}
	}

	return &abundants
}

func isAbundant(n int) bool {
	s := 0

	for _, f := range getFactors(n) {
		s += f
		if s > n {
			return true
		}
	}

	return false
}

func getFactors(n int) []int {
	factors := []int{1}

	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			factors = append(factors, i)
			if i*i != n {
				factors = append(factors, n/i)
			}
		}
	}

	return factors
}
