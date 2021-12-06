package main

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	"testing"
)

func TestFishCounter(t *testing.T) {
	expected := 26
	days := 18
	num := CountFish([]int{3, 4, 3, 1, 2}, days)
	if num != expected {
		t.Errorf("Expected %d got %d\n", expected, num)
	}

	expected = 26984457539
	days = 256
	num = CountFish([]int{3, 4, 3, 1, 2}, days)
	if num != expected {
		t.Errorf("Expected %d got %d\n", expected, num)
	}
}

func TestMainQuestion(t *testing.T) {
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

	expected := 365862
	num := CountFish(ages, 80)
	if num != expected {
		t.Errorf("Expected %d got %d\n", expected, num)
	}

	expected = 1653250886439
	num = CountFish(ages, 256)
	if num != expected {
		t.Errorf("Expected %d got %d\n", expected, num)
	}
}
