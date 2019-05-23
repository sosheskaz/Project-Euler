package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"os/exec"
	"syscall"
	"time"
)

type Result struct {
	Average      float64
	Min          float64
	Max          float64
	Times        []float64
	AverageMem   int
	MinMem       int
	MaxMem       int
	MemUsages    []int
	AverageUTime float64
	MinUTime     float64
	MaxUTime     float64
	UTimes       []float64
	AverageSTime float64
	MinSTime     float64
	MaxSTime     float64
	STimes       []float64
	Count        int
	Command      []string
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
	var rsses []int
	var utimes []float64
	var stimes []float64

	for c := 0; c < count; c++ {
		cmd := exec.Command(args[0], args[1:]...)

		start := time.Now()
		err := cmd.Run()
		end := time.Now()

		delta := end.Sub(start).Seconds()
		times = append(times, delta)

		usage := cmd.ProcessState.SysUsage().(*syscall.Rusage)
		rsses = append(rsses, int(usage.Maxrss))
		const nanoAdjust = 1000000000
		utimes = append(utimes, float64(usage.Utime.Nano())/nanoAdjust)
		stimes = append(stimes, float64(usage.Stime.Nano())/nanoAdjust)

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

	var memSum int
	minMem := math.MaxInt64
	maxMem := math.MinInt64
	for _, mem := range rsses {
		memSum += mem
		if mem > maxMem {
			maxMem = mem
		}
		if mem < minMem {
			minMem = mem
		}
	}
	memAverage := memSum / count

	var utimeSum float64
	minUTime := math.Inf(1)
	maxUTime := math.Inf(-1)
	for _, utime := range utimes {
		utimeSum += utime
		if utime > maxUTime {
			maxUTime = utime
		}
		if utime < minUTime {
			minUTime = utime
		}
	}
	utimeAverage := utimeSum / float64(count)

	var stimeSum float64
	minSTime := math.Inf(1)
	maxSTime := math.Inf(-1)
	for _, stime := range stimes {
		stimeSum += stime
		if stime > maxSTime {
			maxSTime = stime
		}
		if stime < minSTime {
			minSTime = stime
		}
	}
	stimeAverage := stimeSum / float64(count)

	result := &Result{
		Command:      args,
		Count:        count,
		Average:      average,
		Min:          min,
		Max:          max,
		Times:        times,
		AverageMem:   memAverage,
		MinMem:       minMem,
		MaxMem:       maxMem,
		MemUsages:    rsses,
		AverageUTime: utimeAverage,
		MinUTime:     minUTime,
		MaxUTime:     maxUTime,
		UTimes:       utimes,
		AverageSTime: stimeAverage,
		MinSTime:     minSTime,
		MaxSTime:     maxSTime,
		STimes:       stimes}

	answer, _ := json.Marshal(result)
	fmt.Println(string(answer))
}
