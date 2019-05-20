package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	const target = 1000000
	threadCount := runtime.NumCPU()

	var wg sync.WaitGroup
	collatzChains := make(chan []int)
	numbers := count(1, target)

	wg.Add(threadCount)
	for threadIndex := 0; threadIndex < threadCount; threadIndex++ {
		go func() {
			defer wg.Done()

			for n := range numbers {
				collatzChains <- collatz(n)
			}
		}()
	}

	go func() {
		wg.Wait()
		close(collatzChains)
	}()

	biggestChain := make([]int, threadCount)
	biggestStartingNumber := make([]int, threadCount)
	var biggestWg sync.WaitGroup
	biggestWg.Add(threadCount)

	for i, _ := range biggestChain {
		index := i
		go func() {
			defer biggestWg.Done()
			for chain := range collatzChains {
				l := len(chain)
				if l > biggestChain[index] {
					biggestChain[index] = len(chain)
					biggestStartingNumber[index] = chain[0]
				}
			}
		}()
	}

	biggestWg.Wait()
	realBiggestStarting := -1
	realBiggestChain := -1
	for idx, _ := range biggestChain {
		if biggestChain[idx] > realBiggestChain {
			realBiggestChain = biggestChain[idx]
			realBiggestStarting = biggestStartingNumber[idx]
		}
	}

	fmt.Println(realBiggestStarting)
}

func count(from int, to int) <-chan int {
	output := make(chan int)

	go func() {
		for i := from; i < to; i++ {
			output <- i
		}
		close(output)
	}()

	return output
}

func collatz(n int) []int {
	var output []int

	for n > 1 {
		output = append(output, n)
		if n%2 == 0 {
			n /= 2
		} else {
			n = 3*n + 1
		}
	}
	output = append(output, n)

	return output
}
