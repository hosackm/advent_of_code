package main

import (
	"errors"
	"fmt"
	"log"
	"strings"
)

const SPAWN_AGE = 8
const RESPAWN_TO_AGE = 6

type Fish struct {
	Age int
}

func NewFish(age int) (*Fish, error) {
	if age > 8 {
		return nil, errors.New("max age of fish is 8")
	}

	return &Fish{Age: age}, nil
}

// Tick ages a fish by 1 day and returns True if a new fish is spawned otherwise False
func (f *Fish) Tick() bool {
	if f.Age == 0 {
		f.Age = RESPAWN_TO_AGE
		return true
	}

	f.Age--
	return false
}

func (f *Fish) String() string {
	return fmt.Sprintf("%d", f.Age)
}

type School struct {
	Fishes []*Fish
	Day    int
}

func NewSchool(ages ...int) (*School, error) {
	s := School{Day: 0}

	for _, age := range ages {
		f, err := NewFish(age)
		if err != nil {
			return nil, err
		}
		s.Fishes = append(s.Fishes, f)
	}

	return &s, nil
}

func (s *School) GetDisplay() string {
	ages := []string{}
	for _, f := range s.Fishes {
		ages = append(ages, f.String())
	}

	allFish := strings.Join(ages, ",")
	if s.Day == 0 {
		return fmt.Sprintf("initial state: %s", allFish)
	} else {
		return fmt.Sprintf("day %d: %s", s.Day, allFish)
	}
}

func (s *School) Display() {
	log.Println(s.GetDisplay())
}

func (s *School) Tick(display bool) {
	count := 0
	for _, f := range s.Fishes {
		spawn := f.Tick()
		if spawn {
			count++
		}
	}

	if display {
		s.Display()
	}

	s.Day++
	for i := 0; i < count; i++ {
		// add a fish
		f, err := NewFish(SPAWN_AGE)
		if err != nil {
			log.Fatalf("couldn't add a fish of age %d\n", SPAWN_AGE)
		}
		s.Fishes = append(s.Fishes, f)
	}
}
