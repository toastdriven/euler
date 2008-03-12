#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=9
for a in range(1000):
	for b in range(a, 1000 - a):
		c = 1000 - (a + b)
		
		if a**2 + b**2 == c**2:
			answer = int(a * b * c)
			
print answer