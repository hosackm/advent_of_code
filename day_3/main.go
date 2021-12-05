package main

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

type Measurement struct {
	Gamma   int
	Epsilon int
	Oxygen  int
}

func (m Measurement) Product() int {
	return m.Gamma * m.Epsilon
}

func bitSet(n int64, b int) bool {
	return n>>b&1 == 1
}

func countOneBits(numbers []int64, n int) Measurement {
	numBits := n
	numFirstBits := make([]int64, numBits)
	for i := range numFirstBits {
		numFirstBits[i] = 0
	}

	for _, n := range numbers {
		for i := 0; i < numBits; i++ {
			if bitSet(n, i) {
				numFirstBits[numBits-1-i]++
			}
		}
	}

	gamma := 0
	epsilon := 0
	half := len(numbers) / 2
	for i, n := range numFirstBits {
		if int(n) > half {
			gamma += 1 << (numBits - 1 - i)
		} else {
			epsilon += 1 << (numBits - 1 - i)
		}
	}

	m := Measurement{}

	var oxygen []int64
	copy(oxygen, numbers)
	for i := 0; i < numBits; i++ {
		keepers := []int64{}

		if len(oxygen) == 1 {
			m.Oxygen = int(oxygen[0])
			break
		}

		for _, n := range oxygen {
			if int(numFirstBits[i]) > half {
				// keep oxygen
				if bitSet(n, i) {
					keepers = append(keepers, n)
				}
			}
		}

		copy(oxygen, keepers)
	}

	m.Gamma = gamma
	m.Epsilon = epsilon
	return m
}

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal("couldn't read input.txt")
	}

	lines := strings.Split(string(b), "\n")
	numBits := len(lines[0])
	numbers := make([]int64, len(lines))
	for i, line := range lines {
		n, err := strconv.ParseInt(line, 2, 64)
		if err != nil {
			log.Fatal("Couldn't parse int from string encoded binary number:", line)
		}
		numbers[i] = n
	}

	m := countOneBits(numbers, numBits)
	log.Println(m)
	log.Println(m.Product())
}
