package main

import (
	"io/ioutil"
	"log"
	"os"
	"strings"
)

func calculateEndingPoint(commands []*Command) Point {
	loc := Point{0, 0, 0}

	for _, cmd := range commands {
		switch cmd.Direction {
		case "forward":
			loc.Forward(cmd.Distance)
		case "down":
			loc.Down(cmd.Distance)
		case "up":
			loc.Up(cmd.Distance)
		}
	}

	return loc
}

func parseCommands(filename string) []*Command {
	f, err := os.Open("input.txt")
	if err != nil {
		log.Fatal("Couldn't open file")
	}

	fileBytes, err := ioutil.ReadAll(f)
	if err != nil {
		log.Fatal("Error reading file.")
	}

	lines := strings.Split(string(fileBytes), "\n")

	commands := make([]*Command, len(lines))
	for i, line := range lines {
		c, err := CommandFromString(line)
		if err != nil {
			log.Fatal(err)
		}
		commands[i] = c
	}
	return commands
}

func main() {
	commands := parseCommands("input.txt")
	end := calculateEndingPoint(commands)
	log.Printf("Final location (%d, %d) -> %d\n",
		end.Horizontal, end.Depth, end.Horizontal*end.Depth)
}
