#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=12
import math
from EulerLibs import MathLibs

factors = 0
cursor = 0
while (factors <= 500):
	cursor += 1
	answer = MathLibs.triangleNumber(cursor)
	factors = len(MathLibs.factors(answer))
	
print answer