package main

import (
	"fmt"
)

func main() {
	const n = 101
	sumOfSquares := SumOfSquares(1, n)
	squareOfSum := SquareOfSum(1, n)
	result := squareOfSum - sumOfSquares
	fmt.Println(result)
}

func SquareOfSum(start int, end int) int {
	sum := 0
	for i := start; i < end; i++ {
		sum += i
	}
	return sum * sum
}

func SumOfSquares(start int, end int) int {
	sum := 0
	for i := start; i < end; i++ {
		sum += i * i
	}
	return sum
}
