package main

import (
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

func numIncreasesNoWindow(measurements []int) int {
	numIncreases := 0
	numLines := len(measurements)

	last := measurements[0]

	for i := 1; i < numLines; i++ {
		m := measurements[i]
		if m > last {
			numIncreases++
		}
		last = m
	}
	return numIncreases
}

func numIncreasesWindow(meas []int) int {
	winSize := 3
	numIncreases := 0

	last := meas[0] + meas[1] + meas[2]
	for i := 1; i <= len(meas)-winSize; i++ {
		this := meas[i] + meas[i+1] + meas[i+2]
		if this > last {
			numIncreases++
		}
		last = this
	}
	return numIncreases
}

func main() {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	rbytes, err := ioutil.ReadAll(f)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(rbytes), "\n")
	measurements := make([]int, len(lines))
	for i := 0; i < len(lines); i++ {
		n, err := strconv.Atoi(lines[i])
		if err != nil {
			log.Fatal("Error converting line to int:", lines[i])
		}
		measurements[i] = n
	}

	numIncreases := numIncreasesNoWindow(measurements)
	log.Println("Number of increases is:", numIncreases)

	numIncreases = numIncreasesWindow(measurements)
	log.Println("Number of increases (with window) is:", numIncreases)
}
