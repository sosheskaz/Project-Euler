package main

import (
	"container/list"
	"fmt"
	"math"
)

func main() {
	const max = 20

	// We need this multiple times later. Pre-calculate it.
	const maxFloat = float64(max)

	primeList := primes(max)
	product := 1

	for prime := primeList.Front(); prime != nil; prime = prime.Next() {
		// ln(a) / ln(b) is equivalent to log(a) base b.
		val := float64(prime.Value.(int))

		numer := math.Log(maxFloat)
		denom := math.Log(val)
		pow := math.Floor(numer / denom)

		product *= int(math.Pow(val, pow))
	}

	fmt.Println(product)
}

func primes(upTo int) *list.List {
	primeList := list.New()
	if upTo < 2 {
		fmt.Println("skipping")
		return primeList
	}

	primeList.PushBack(2)

	for i := 3; i < upTo; i += 2 {
		var isPrime bool = true

		for prime := primeList.Front(); prime != nil; prime = prime.Next() {
			if i % prime.Value.(int) == 0 {
				isPrime = false
				break
			}
		}

		if isPrime {
			primeList.PushBack(i)
		}
	}

	return primeList
}
