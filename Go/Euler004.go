package main

import "strconv"
import "fmt"

func main() {
	var biggest = -1

	for a := 100; a < 1000; a++ {
		for b := a + 1; b < 1000; b++ {
			product := a * b
			productString := strconv.Itoa(product)
			if product > biggest && productString == reverse(productString) {
				biggest = product
			}
		}
	}

	fmt.Println(biggest)
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
