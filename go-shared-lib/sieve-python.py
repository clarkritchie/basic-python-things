#!/usr/bin/env python3
def sieve(n):
	a = set()
	s = [2]
	m = int(round(n/2.0))
	for i in range(1, n):
		for j in range(i, n):
			p = i + j + 2*i*j
			if (p <= m):
				a.add(p)
	for k in range(1, m):
		if (k not in a):
			q = 2*k + 1
			s.append(q)
	return s

sieve(10000)
print("all done, python")