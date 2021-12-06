package main

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {
	b, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal("couldn't read input.txt")
	}

	ages := []int{}
	for _, n := range strings.Split(string(b), ",") {
		num, err := strconv.Atoi(n)
		if err != nil {
			log.Fatalf("couldn't convert %s to a number", n)
		}
		ages = append(ages, num)
	}
	log.Println("Calculated sum after 80 days", CountFish(ages, 80))
	log.Println("Calculated sum after 256 days:", CountFish(ages, 256))
}
