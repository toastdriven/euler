#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=23
from EulerLibs import MathLibs

most_primes = { 'a': 1, 'b': 41, 'primes': 40 }

for a in xrange(-999, 1000):
	for b in xrange(-999, 1000):
		n = 0
		prime_count = 0
		while True:
			p = n**2 + (a * n) + b
			if p < 2:
				break
			elif not MathLibs.isPrime(p):
				break
				
			prime_count += 1
			n += 1
			
		values = { 'a': a, 'b': b, 'primes': prime_count }
		
		if values['primes'] > most_primes['primes']:
			most_primes = values
			
answer = most_primes['a'] * most_primes['b']
print answer