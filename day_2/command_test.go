package main

import (
	"testing"
)

func TestCommandParseFromString(t *testing.T) {
	type TestInput struct {
		Stimulus string
		Cmd      Command
	}
	inputs := []TestInput{
		{"Up 0", Command{Direction: "up", Distance: 0}},
		{"up 2", Command{Direction: "up", Distance: 2}},
		{"up -1", Command{Direction: "up", Distance: -1}},
		{"Forward 7", Command{Direction: "forward", Distance: 7}},
		{"forward 0", Command{Direction: "forward", Distance: 0}},
		{"forward -1", Command{Direction: "forward", Distance: -1}},
		{"down -1", Command{Direction: "down", Distance: -1}},
		{"Down 0", Command{Direction: "down", Distance: 0}},
		{"down 42", Command{Direction: "down", Distance: 42}},
	}

	for _, i := range inputs {
		cmd, _ := CommandFromString(i.Stimulus)
		if cmd.Direction != i.Cmd.Direction || cmd.Distance != i.Cmd.Distance {
			t.Fail()
		}
	}
}

func TestBadInputReturnsErrors(t *testing.T) {
	inputs := []string{"orward 2", "up a", "down", "blargh", "42 forward"}
	for _, i := range inputs {
		_, err := CommandFromString(i)
		if err == nil {
			t.Fail()
		}
	}
}
