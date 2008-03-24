#!/usr/bin/env python
# Libraries to make my life shorter
# @author Luke Sneeringer
import math

class MathLibs:
	@staticmethod
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

	@staticmethod
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
		
	@staticmethod
	def factorial(x):
		return reduce(lambda x, y: x * y, [i for i in range(1, int(x) + 1)])
		
		
	@staticmethod
	def triangleNumber(x):
		return x * (x + 1) / 2
		#return reduce(lambda x, y: x + y, [i for i in range(1, int(x) + 1)])
		
	@classmethod
	def sumOfDivisors(cls, x):
		factors = cls.factors(x)
		if len(factors):
			factors.pop()
			return sum(factors)
		else:
			return 0
		
	
class StrLibs:
	@staticmethod
	def isPalindrome(s):
		i = 0
		while i <= math.ceil(len(s) / 2):
			if not s[i] == s[len(s) - i - 1]:
				return False;
			i += 1
		return True

	@staticmethod
	def sumDigits(s):
		return int(reduce(lambda x, y: int(x) + int(y), s))