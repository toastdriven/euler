#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=7
import math
from EulerLibs import MathLibs

primes = 0
answer = 1;
while (primes < 10001):
	answer += 1
	if (MathLibs.isPrime(answer)):
		primes += 1	
	
print answer