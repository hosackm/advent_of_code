package main

import (
	"errors"
	"fmt"
	"strings"
)

type Command struct {
	Direction string
	Distance  int
}

func CommandFromString(s string) (*Command, error) {
	c := Command{}
	n, err := fmt.Sscanf(s, "%s %d", &c.Direction, &c.Distance)
	if err != nil || n != 2 {
		return &c, errors.New("couldn't parse direction and magnitude from string")
	}
	c.Direction = strings.ToLower(c.Direction)

	if c.Direction != "up" && c.Direction != "down" && c.Direction != "forward" {
		return &c, fmt.Errorf("%s is not a valid direction", c.Direction)
	}

	return &c, nil
}
