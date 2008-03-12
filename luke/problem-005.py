#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=4
import math
from EulerLibs import MathLibs

# find the product of all numbers between 1 and x
# @return int
def product_1_to_x(x):
	resp = 1
	for i in range(2,x):
		resp *= i
	
	return resp
	
common_factor = product_1_to_x(20)
	
answer = 0
for i in MathLibs.factors(common_factor):
	j = 1
	disproven = False
	while j <= 20 and not disproven:
		if i % j:
			disproven = True
		j += 1
		
		if j == 20:
			answer = i
	
	if answer:
		break
			
print answer