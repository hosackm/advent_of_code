package main

import (
	"testing"
)

func TestFishStartsAtDefaultAge(t *testing.T) {
	fish, err := NewFish(SPAWN_AGE)
	if err != nil {
		t.Fail()
	}
	if fish.Age != SPAWN_AGE {
		t.Fail()
	}
}

func TestFishDecrementsAndLoops(t *testing.T) {
	fish, err := NewFish(SPAWN_AGE)
	if err != nil {
		t.Fail()
	}

	fish.Tick()
	if fish.Age != SPAWN_AGE-1 {
		t.Fail()
	}

	for i := 1; i <= SPAWN_AGE; i++ {
		fish.Tick()
	}
	if fish.Age != RESPAWN_TO_AGE {
		t.Fail()
	}
}

func TestInitialFishesStartWithCorrectAges(t *testing.T) {
	ages := []int{3, 4, 3, 1, 2}
	s, err := NewSchool(ages...)
	if err != nil {
		t.Errorf("NewSchool returned error %s", err.Error())
	}

	for i, f := range s.Fishes {
		if f.Age != ages[i] {
			t.Errorf("Age %d doesn't match expected %d\n", f.Age, ages[i])
		}
	}
}

func TestFishesAgeAndSpawnAsExplainedInExample(t *testing.T) {
	// From example input
	startingAges := []int{3, 4, 3, 1, 2}

	s, err := NewSchool(startingAges...)
	if err != nil {
		t.Error("couldn't initialize the school to start")
	}

	displayStrings := []string{
		"initial state: 3,4,3,1,2",
		"day 1: 2,3,2,0,1",
		"day 2: 1,2,1,6,0,8",
		"day 3: 0,1,0,5,6,7,8",
		"day 4: 6,0,6,4,5,6,7,8,8",
		"day 5: 5,6,5,3,4,5,6,7,7,8",
		"day 6: 4,5,4,2,3,4,5,6,6,7",
		"day 7: 3,4,3,1,2,3,4,5,5,6",
		"day 8: 2,3,2,0,1,2,3,4,4,5",
		"day 9: 1,2,1,6,0,1,2,3,3,4,8",
		"day 10: 0,1,0,5,6,0,1,2,2,3,7,8",
		"day 11: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8",
		"day 12: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8",
		"day 13: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8",
		"day 14: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8",
		"day 15: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7",
		"day 16: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8",
		"day 17: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8",
		"day 18: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8",
	}

	for i := 0; i < len(displayStrings); i++ {
		str := s.GetDisplay()
		expected := displayStrings[i]
		if str != expected {
			t.Errorf("'%s' doesn't match '%s'", str, expected)
		}
		s.Tick(false)
	}
}

func TestNumFishesAfter80DaysMatches(t *testing.T) {
	numDays := 80
	numFishes := 5934
	s, _ := NewSchool([]int{3, 4, 3, 1, 2}...)
	for i := 0; i < numDays; i++ {
		s.Tick(false)
	}

	if len(s.Fishes) != numFishes {
		t.Errorf("num fishes after %d days should be %d, got %d", numDays, numFishes, len(s.Fishes))
	}
}
