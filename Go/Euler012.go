package main

import (
	"fmt"
	"math"
)

func main() {
	const target = 500

	triangle := 0
	incrementer := 1
	for len(getDivisors(triangle)) < target {
		triangle += incrementer
		incrementer++
	}

	fmt.Println(triangle)
}

func getDivisors(num int) map[int]struct{} {
	max := int(math.Ceil(math.Sqrt(float64(num))))
	divisors := make(map[int]struct{})

	for i := 2; i <= max; i++ {
		if num%i == 0 {
			divisors[i] = struct{}{}
			divisors[num/i] = struct{}{}
		}
	}

	return divisors
}
