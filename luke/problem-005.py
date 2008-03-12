#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=4
import math
from EulerLibs import MathLibs

# Find a common denominator of 1 to x
# @return int
def common_denom(x):
	resp = 1
	while x >= 1:
		if resp % x:
			resp *= x
			
		x -= 1
	
	return resp
	
common_factor = common_denom(20)
	
answer = 0
for i in MathLibs.factors(common_factor):
	j = 1
	disproven = False
	while j <= 20 and not disproven:
		if i % j:
			disproven = True
			
		if j == 20:
			answer = i

		j += 1
		
	
	if answer:
		break
			
print answer