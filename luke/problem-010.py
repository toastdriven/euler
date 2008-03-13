#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=10
import math
from EulerLibs import MathLibs

prime_numbers = range(2, 2000000 + 1)
for i in prime_numbers:
	if i > 0:
		j = 2 * i - 2 
		while j <= (2000000 - 2):
			prime_numbers[j] = 0
			j += i
			
answer = sum(prime_numbers)
print answer