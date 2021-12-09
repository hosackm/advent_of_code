package main

import "testing"

func TestStartsEmpty(t *testing.T) {
	s := NewSet()
	if s.Has("a") {
		t.Error("empty set shouldn't have 'a'")
	}
}

func TestAddCanBeHad(t *testing.T) {
	s := NewSet()
	input := []string{"a", "b", "c", "d"}
	for _, v := range input {
		s.Add(v)
		if !s.Has(v) {
			t.Errorf("set should have '%s'", v)
		}
	}
}

func TestNewSetWithSetsCorrectKeys(t *testing.T) {
	s := NewSetWith("a", "b")
	if !s.Has("a") || !s.Has("b") {
		t.Error("set should have 'a' and 'b'")
	}
}

func TestDiffReturnsCorrectSetDifference(t *testing.T) {
	s := NewSetWith("a", "b", "c")
	s2 := NewSetWith("b", "c", "d")
	s3 := s.Diff(s2)
	if !s3.Has("a") {
		t.Error("set should have 'a'")
	}
	if !s3.Has("d") {
		t.Error("set should have 'd'")
	}
}

func TestSubReturnsCorrectSetComplement(t *testing.T) {
	s := NewSetWith("a", "b", "c")
	s2 := NewSetWith("b", "c", "d")
	s3 := s.Sub(s2)
	if !s3.Has("a") {
		t.Error("set should have 'a'")
	}
	if s3.Has("d") {
		t.Error("set shouldn't have 'd'")
	}
}
