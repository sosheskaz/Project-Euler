package main

import (
	"fmt"
	"math"
)

type Cart struct {
	x int
	y int
}

func main() {
	const squareLen = 20

	fmt.Println(combinatoric(squareLen*2, squareLen))
}

func combinatoric(n int, r int) int {
	numer := factorial(n)
	denom := factorial(r) * factorial(n-r)
	return int(math.Round(numer / denom))
}

func factorial(n int) float64 {
	p := 1.0
	for x := n; x > 1; x-- {
		p *= float64(x)
	}
	return (p)
}

// func main() {
// 	maxPos := Cart{
// 		x: 20,
// 		y: 20,
// 	}
// 	startPos := Cart{
// 		x: 0,
// 		y: 0,
// 	}

// 	fmt.Println(countPaths(startPos, maxPos))
// }

// func countPaths(position Cart, maximum Cart) int {
// 	paths := 0

// 	if position.x == maximum.x && position.y == maximum.y {
// 		return paths + 1
// 	}

// 	if position.x < maximum.x {
// 		nextPoint := Cart{
// 			x: position.x + 1,
// 			y: position.y,
// 		}
// 		paths += countPaths(nextPoint, maximum)
// 	}

// 	if position.y < maximum.y {
// 		nextPoint := Cart{
// 			x: position.x,
// 			y: position.y + 1,
// 		}
// 		paths += countPaths(nextPoint, maximum)
// 	}

// 	return paths
// }
