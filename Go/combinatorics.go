package main

import "fmt"

// Based on Python's itertools implementation
func GetCombinations(source []int, r int) (<-chan []int, error) {
	if r < 0 {
		return nil, fmt.Errorf("GetCombinations: r must be >= 0; got %d", r)
	}

	pool := make([]int, len(source))
	copy(pool, source)
	n := len(pool)
	if r > n {
		return nil, fmt.Errorf("r (%d) cannot be greater than the size of the source pool (%d)", r, n)
	}

	c := make(chan []int)
	go func() {
		defer close(c)

		indices := make([]int, r)
		for idx, _ := range indices {
			indices[idx] = idx
		}

		previous := make([]int, r)
		current := make([]int, r)
		var i int
		var j int

		for i, index := range indices {
			current[i] = pool[index]
		}
		c <- current

		for true {
			copy(previous, current)
			current = make([]int, r)

			for i = r - 1; i >= 0 && indices[i] == i+n-r; i-- {
			}

			if i < 0 {
				break
			}

			indices[i]++
			for j = i + 1; j < r; j++ {
				indices[j] = indices[j-1] + 1
			}

			for i, index := range indices {
				current[i] = pool[index]
			}

			c <- current
		}
	}()

	return c, nil
}

func GetCombinationsWithReplacement(source []int, r int) (<-chan []int, error) {
	if r < 0 {
		return nil, fmt.Errorf("GetCombinations: r must be >= 0; got %d", r)
	}

	pool := make([]int, len(source))
	copy(pool, source)
	n := len(pool)

	c := make(chan []int)
	go func() {
		defer close(c)

		indices := make([]int, r)
		current := make([]int, r)
		var i int
		var j int

		for i, index := range indices {
			current[i] = pool[index]
		}
		c <- current

		for true {
			current = make([]int, r)

			for i = r - 1; i >= 0 && indices[i] == n-1; i-- {
			}

			if i < 0 {
				break
			}

			indices[i]++
			for j = i + 1; j < r; j++ {
				indices[j] = indices[j-1]
			}

			for i, index := range indices {
				current[i] = pool[index]
			}

			c <- current
		}
	}()

	return c, nil
}
