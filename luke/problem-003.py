#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=3
import math

def factors(x):
	factors = []
	
	i = 1
	while i <= math.ceil(math.sqrt(x)):
		if not x % i:
			if not factors.count(i):
				factors.append(i)
				if not factors.count(x / i): # don't add perfect squares twice
					factors.append(x / i)
				factors.sort()
		
		i += 1
			
	return factors
	
def isPrime(x):
	i = 2
	while i <= math.ceil(math.sqrt(x)):
		if not x % i:
			return False
			
		i += 1
	
	return True

answer = 0
for i in factors(600851475143):
	if isPrime(i):
		answer = i
		
print answer