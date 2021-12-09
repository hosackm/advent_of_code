package main

type Set map[string]bool

func NewSet() Set {
	return Set{}
}

func NewSetWith(keys ...string) Set {
	ret := Set{}
	for _, s := range keys {
		ret.Add(s)
	}
	return ret
}

func (s Set) Add(c string) {
	s[c] = true
}

func (s Set) Has(c string) bool {
	_, ok := s[c]
	return ok
}

func (s Set) Sub(other Set) Set {
	result := NewSet()
	for k := range s {
		if !other.Has(k) {
			result.Add(k)
		}
	}
	return result
}

func (s Set) Diff(other Set) Set {
	result := NewSet()
	for k := range s {
		if !other.Has(k) {
			result[k] = s[k]
		}
	}

	for k := range other {
		if !s.Has(k) {
			result[k] = s[k]
		}
	}

	return result
}
