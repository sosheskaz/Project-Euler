package main

import "fmt"

func main() {
	sum := 0

	for i := 3; i < 1000; i += 3 {
		sum += i
	}

	for i := 5; i < 1000; i += 5 {
		if i%3 == 0 {
			continue
		}
		sum += i
	}

	fmt.Println(sum)
}
