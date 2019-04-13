package main

import (
	"flag"
	"encoding/json"
	"log"
	"math"
	"os"
	"os/exec"
	"time"
	"fmt"
)

type Result struct {
	Average float64
	Min float64
	Max float64
	Times []float64
	Count int
	Command []string
}

func main() {
	countPtr := flag.Int("count", 10, "Number of times to run.")
	helpPtr := flag.Bool("help", false, "Display this help message.")
	flag.Parse()

	count := *countPtr
	help := *helpPtr

	if help {
		flag.PrintDefaults()
		os.Exit(1)
	}

	args := flag.Args()

	var times []float64
	for c := 0; c < count; c++ {
		cmd := exec.Command(args[0], args[1:]...)

		start := time.Now()
		err := cmd.Run()
		end := time.Now()

		delta := end.Sub(start).Seconds()
		times = append(times, delta)

		if err != nil {
			log.Fatal(err)
			os.Exit(2)
		}
	}

	var sum float64
	min := math.Inf(1)
	max := math.Inf(-1)
	for _, time := range times {
		sum += time
		if time > max {
			max = time
		}
		if time < min {
			min = time
		}
	}
	average := sum / float64(count)

	result := &Result{
		Average: average,
		Command: args,
		Count: count,
		Min: min,
		Max: max,
		Times: times}

	answer, _ := json.Marshal(result)
	fmt.Println(string(answer))
}
