package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	const factorCt = 13

	const char0 = 48
	const char9 = 57

	dat, err := ioutil.ReadFile("input/Euler008.txt")
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	// Keep track of the last n digits in this circular buffer.
	buffer := make([]int, factorCt)

	var product int
	var nextProduct int
	for index, charbyte := range dat {
		if charbyte < char0 || charbyte > char9 {
			continue
		}

		buffer[index%len(buffer)] = int(charbyte - char0)

		nextProduct = productOfBuffer(&buffer)
		if nextProduct > product {
			product = nextProduct
		}
	}

	fmt.Println(product)
}

func productOfBuffer(bufferPtr *[]int) int {
	buffer := *bufferPtr
	product := 1
	for _, value := range buffer {
		product *= value
	}

	return product
}
