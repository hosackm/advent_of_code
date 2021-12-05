package main

type Point struct {
	Horizontal int
	Depth      int
	Aim        int
}

func (p *Point) Up(x int) {
	p.Aim -= x
}

func (p *Point) Forward(x int) {
	p.Horizontal += x
	p.Depth += p.Aim * x
}

func (p *Point) Down(x int) {
	p.Aim += x
}
