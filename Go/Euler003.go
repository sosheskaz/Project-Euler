package main

import "fmt"

func main() {
	var slice = primeFactors(600851475143)
	fmt.Println(slice[len(slice)-1])
}

func primeFactors(ofNumber int) []int {
	var factors []int

	for ofNumber%2 == 0 {
		ofNumber /= 2
		factors = append(factors, 2)
	}

	for i := 3; i <= ofNumber; i += 2 {
		if ofNumber == 1 {
			break
		}

		for ofNumber%i == 0 {
			ofNumber /= i
			factors = append(factors, i)
		}
	}

	return factors
}
