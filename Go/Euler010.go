package main

import (
	"fmt"
)

func main() {
	const target = 2000000

	primes := Sieve(target)
	sum := 0
	for _, prime := range primes {
		sum += prime
	}

	fmt.Println(sum)
}
