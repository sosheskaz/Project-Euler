package main

import "fmt"

func CombinationsWithReplacement(src []int, count int) (<-chan []int, error) {
	if count < 1 {
		return nil, fmt.Errorf("Error: Argument 'count' cannot be less than 1, got: %d", count)
	}

	c := make(chan []int)

	go func() {
		defer close(c)

		if count == 1 {
			for _, item := range src {
				c <- []int{item}
			}
		} else {
			for idx, item := range src {
				combos, _ := CombinationsWithReplacement(src[idx:], count-1)
				for baseResult := range combos {
					c <- append(baseResult, item)
				}
			}
		}
	}()

	return c, nil
}
