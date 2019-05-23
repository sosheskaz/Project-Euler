package main

import (
	"fmt"
	"math/big"
)

func main() {
	const targetInt = 100
	var target *big.Int
	target = big.NewInt(targetInt)

	result := factorial(target)

	big10 := big.NewInt(10)
	big0 := big.NewInt(0)

	var sum int64
	digit := big.NewInt(0)

	for result.Cmp(big0) == 1 {
		result.DivMod(result, big10, digit)
		sum += digit.Int64()
	}

	fmt.Println(sum)
}

func factorial(n *big.Int) *big.Int {
	big1 := big.NewInt(1)
	fact := big.NewInt(1)

	for counter := n; n.Cmp(big1) == 1; counter.Sub(counter, big1) {
		fact.Mul(fact, n)
	}
	return fact
}
