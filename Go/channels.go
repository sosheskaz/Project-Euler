package main

import "fmt"

func main() {
	c := sender()
	for i := range c {
		fmt.Println(i)
	}
}

func sender() <-chan int {
	c := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			c <- i
		}
		close(c)
	}()
	return c
}
