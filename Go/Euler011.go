package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	x int
	y int
}

// Note that this implementation *only* works if nRows = nCols
func main() {
	const target = 4
	tablePtr := LoadFile("input/Euler011.txt")
	// biggest := MaxProduct(tablePtr, target)
	// fmt.Println(biggest)

	// We need to multiplex the inputs to allow multiple consumers
	points := TablePoints(tablePtr)
	input := Multiplex(points, 4)

	horiz := HorizSlices(tablePtr, input[0], target)
	vert := VertSlices(tablePtr, input[1], target)
	diagWest := DiagWestSlices(tablePtr, input[2], target)
	diagEast := DiagEastSlices(tablePtr, input[3], target)

	pHoriz, pVert, pDW, pDE := MulSlices(horiz), MulSlices(vert), MulSlices(diagWest), MulSlices(diagEast)
	maxHoriz, maxVert, maxDW, maxDE := Max(pHoriz), Max(pVert), Max(pDW), Max(pDE)

	maxCandidates := []int{<-maxHoriz, <-maxVert, <-maxDW, <-maxDE}
	max := -1
	for _, mc := range maxCandidates {
		if mc > max {
			max = mc
		}
	}
	fmt.Println(max)
}

func LoadFile(path string) *[][]int {
	dat, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	var result [][]int

	contents := string(dat)
	rowStrings := strings.Split(contents, "\n")
	for _, rowString := range rowStrings {
		var row []int

		values := strings.Split(rowString, " ")
		for _, value := range values {
			if value == "" {
				continue
			}
			intValue, _ := strconv.Atoi(value)
			row = append(row, intValue)
		}

		// Ignore empty lines
		if len(row) > 0 {
			result = append(result, row)
		}
	}

	return &result
}

func Multiplex(input <-chan Point, n int) []chan Point {
	multiplexed := make([]chan Point, n)
	for idx, _ := range multiplexed {
		multiplexed[idx] = make(chan Point)
	}

	go func() {
		for p := range input {
			for _, c := range multiplexed {
				c <- p
			}
		}

		for _, c := range multiplexed {
			close(c)
		}
	}()

	return multiplexed
}

func TablePoints(tablePtr *[][]int) <-chan Point {
	table := *tablePtr
	out := make(chan Point)

	go func() {
		for x := 0; x < len(table); x++ {
			for y := 0; y < len(table[x]); y++ {
				out <- Point{x: x, y: y}
			}
		}
		close(out)
	}()

	return out
}

// Note that, if you look at the table, this is actually vertical. Rotate it in your head.
// Also note that the table is used only for reading
func HorizSlices(tablePtr *[][]int, points <-chan Point, target int) <-chan []int {
	out := make(chan []int)
	table := *tablePtr

	go func() {
		for point := range points {
			if point.x+target > len(table) {
				continue
			}

			slice := make([]int, target)
			for cursor := 0; cursor < target; cursor++ {
				slice[cursor] = table[point.x+cursor][point.y]
			}
			out <- slice
		}

		close(out)
	}()

	return out
}

func VertSlices(tablePtr *[][]int, points <-chan Point, target int) <-chan []int {
	c := make(chan []int)
	table := *tablePtr

	go func() {
		for point := range points {
			if point.y+target > len(table[point.x]) {
				continue
			}

			slice := make([]int, target)
			for cursor := 0; cursor < target; cursor++ {
				slice[cursor] = table[point.x][point.y+cursor]
			}
			c <- slice
		}

		close(c)
	}()

	return c
}

func DiagEastSlices(tablePtr *[][]int, points <-chan Point, target int) <-chan []int {
	out := make(chan []int)
	table := *tablePtr

	go func() {
		for point := range points {
			if point.x+target > len(table) || point.y+target > len(table[point.x]) {
				continue
			}

			slice := make([]int, target)
			for cursor := 0; cursor < target; cursor++ {
				slice[cursor] = table[point.x+cursor][point.y+cursor]
			}
			out <- slice
		}

		close(out)
	}()

	return out
}

func DiagWestSlices(tablePtr *[][]int, points <-chan Point, target int) <-chan []int {
	c := make(chan []int)
	table := *tablePtr

	go func() {
		for point := range points {
			if point.x-target+1 < 0 || point.y+target > len(table[point.x]) {
				continue
			}

			slice := make([]int, target)
			for cursor := 0; cursor < target; cursor++ {
				slice[cursor] = table[point.x-cursor][point.y+cursor]
			}
			c <- slice
		}

		close(c)
	}()

	return c
}

func MulSlices(sliceChannel <-chan []int) <-chan int {
	out := make(chan int)

	go func() {
		for slice := range sliceChannel {
			product := 1
			for _, val := range slice {
				product *= val
			}
			out <- product
		}

		close(out)
	}()

	return out
}

func Max(inputs <-chan int) <-chan int {
	out := make(chan int)

	go func() {
		max := -1
		for n := range inputs {
			if n > max {
				max = n
			}
		}

		out <- max
		close(out)
	}()

	return out
}
