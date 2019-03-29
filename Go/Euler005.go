package main

import "fmt"

func main() {
	// Mapping of prime factor : number of times it's a factor
	intSet := make(map[int]int)
	for i := 2; i <= 20; i++ {
		tmpSet := make(map[int]int)
		for _, factor := range primeFactors(i) {
			if _, ok := tmpSet[factor]; ok {
				tmpSet[factor]++
			} else {
				tmpSet[factor] = 1
			}
			if tmpSet[factor] > intSet[factor] {
				intSet[factor] = tmpSet[factor]
			}
		}
	}

	product := 1
	for prime, frequency := range intSet {
		for i := 0; i < frequency; i++ {
			product *= prime
		}
	}
	fmt.Println(product)
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
