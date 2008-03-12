#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=3
import math
from EulerLibs import MathLibs

answer = 0
for i in MathLibs.factors(600851475143):
	if MathLibs.isPrime(i):
		answer = i
		
print answer