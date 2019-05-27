package main

import (
	"fmt"
	"math"
)

func main() {
	const target = 10000

	properDivisorsSum := make(map[int]int)
	for i := 2; i < target; i++ {
		properDivisorsSum[i] = Sum(ProperDivisors(i)...)
	}

	fmt.Println(properDivisorsSum)
}

func ProperDivisors(n int) []int {
	divisors := []int{1}

	for i := 2; i < int(math.Ceil(math.Sqrt(float64(n)))); i++ {
		if n%i == 0 {
			divisors = append(divisors, i)
			otherDivisor := n / i
			if otherDivisor != i {
				divisors = append(divisors, otherDivisor)
			}
		}
	}

	return divisors
}

func Sum(n ...int) int {
	sum := 0
	for _, i := range n {
		sum += i
	}
	return sum
}
