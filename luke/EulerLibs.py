#!/usr/bin/env python
# Libraries to make my life shorter
# @author Luke Sneeringer
import math

class MathLibs:
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
	factors = staticmethod(factors)

	def isPrime(x):
		# special case
		if x == 2:
			return True
		
		i = 2
		while i <= math.ceil(math.sqrt(x)):
			if not x % i:
				return False

			i += 1

		return True
	isPrime = staticmethod(isPrime)
	
class StrLibs:
	def isPalindrome(s):
		i = 0
		while i <= math.ceil(len(s) / 2):
			if not s[i] == s[len(s) - i - 1]:
				return False;
			i += 1
		return True
	isPalindrome = staticmethod(isPalindrome)