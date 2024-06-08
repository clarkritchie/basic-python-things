package main

import (
    "C"
)

//export Sieve
func Sieve(n int) {
	a := make(map[int]bool)
	s := []int{2}
	m := n/2
	for i := 1; i < n; i++ {
		for j := i; j < n; j++ {
			p := i + j + 2*i*j
			if p <= n {
				a[p] = true
			}
		}
	}
	for k := 1; k < m; k++ {
		if !a[k] {
			q := 2*k + 1
			s = append(s, q)
			fmt.Printf("%d %d\n",s,q)
		}
	}
}

func main() { }
