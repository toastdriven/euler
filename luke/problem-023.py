#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=23
from EulerLibs import MathLibs

abundants = {}
for i in xrange(12,28112):
	if MathLibs.sumOfDivisors(i) > i:
		abundants[i] = True
		
#print abundants
#exit()

answer = 0
for i in xrange(1,28124):
	two_abundants_found = False
	
	for j in abundants:
		if j >= i:
			break
		else:
			if abundants.has_key(i - j):
				two_abundants_found = True
				break
	
	if not two_abundants_found:
		answer += i
		
print answer