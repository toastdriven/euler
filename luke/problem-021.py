#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=21
import math
from EulerLibs import MathLibs

d = []
for i in range(0,10001):
	d.append(MathLibs.sumOfDivisors(i))
	
amicables = []
for i in range(2,10001):
	try:		
		if d[d[i]] == i and d[i] != i:
			amicables.append(i)
	except IndexError:
		pass

answer = sum(amicables)	
print answer