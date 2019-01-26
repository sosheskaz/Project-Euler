package main

import "fmt"

func main() {
	sum := 0

	var previous = 1
	var current = 1
	for current < 4000000 {
		oldPrev := previous
		previous = current
		current = previous + oldPrev

		if current%2 == 0 {
			sum += current
		}
	}

	fmt.Println(sum)
}
