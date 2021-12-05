package main

import "testing"

func TestUpReducesAim(t *testing.T) {
	distances := []int{8, 0, -1, 1000}
	for _, d := range distances {
		p := Point{0, 0, 0}
		p.Up(d)
		if p.Aim != -d || p.Depth != 0 || p.Horizontal != 0 {
			t.Fail()
		}
	}
}

func TestDownIncreasesAim(t *testing.T) {
	distances := []int{7, 0, -3, 1234}
	for _, d := range distances {
		p := Point{0, 0, 0}
		p.Down(d)
		if p.Aim != d || p.Depth != 0 || p.Horizontal != 0 {
			t.Fail()
		}
	}
}

func TestForwardModifiesDepthScaledByAim(t *testing.T) {
	distances := []int{7, 0, -3, 1234}
	points := []Point{
		{Horizontal: 0, Depth: 0, Aim: 1},
		{Horizontal: 0, Depth: 0, Aim: 10},
		{Horizontal: 0, Depth: 0, Aim: -13},
		{Horizontal: 0, Depth: 0, Aim: 0},
	}

	for _, d := range distances {
		for _, p := range points {
			beforeDepth := p.Depth

			p.Forward(d)
			if p.Depth != beforeDepth+d*p.Aim {
				t.Fail()
			}
			if p.Horizontal != d {
				t.Fail()
			}
		}
	}
}

func TestUpAndDownCancelOut(t *testing.T) {
	distances := []int{7, 0, -3, 1234}
	for _, d := range distances {
		p := Point{0, 0, 0}
		p.Down(d)
		p.Up(d)
		if p.Aim != 0 {
			t.Fail()
		}
	}
}
