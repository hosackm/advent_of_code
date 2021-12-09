package main

import (
	"io/ioutil"
	"log"
	"strings"
)

type Measurement struct {
	Readings []string
	Display  []string
}

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal("couldn't read input.txt")
	}

	lines := strings.Split(string(b), "\n")
	measurements := make([]Measurement, len(lines))
	for i, line := range lines {
		parts := strings.Split(line, "|")
		rawReading, rawDisplay := parts[0], parts[1]
		measurements[i].Readings = strings.Split(rawReading, " ")
		measurements[i].Display = strings.Split(rawDisplay, " ")
	}

	count := 0
	for _, m := range measurements {
		for _, display := range m.Display {
			n := len(display)
			switch n {
			case 2, 3, 4, 7:
				count++
			}
		}
	}

	log.Printf("Found %d instances of 1, 4, 7, or 8 \n", count)
}
