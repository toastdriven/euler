#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=4
import math

def is_palindrome(s):
	i = 0
	while i <= math.ceil(len(s) / 2):
		if not s[i] == s[len(s) - i - 1]:
			return False;
		i += 1
	return True
	
i = 999 * 999
answer = 0
while True:
	if is_palindrome(str(i)):
		# check and see if it is the product of two three-digit numbers
		j = 999
		while j >= 100:
			if (not i % j) and (i / j <= 999) and (i / j >= 100):
				# print "%d times %d equals %d" % (j, i / j, i)
				answer = i
				break
			j -= 1
		
		if answer > 0:
			break
			
	i -= 1
	
print answer