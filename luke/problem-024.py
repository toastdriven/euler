#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=24
import math

def moveDigit(x):
	if x == 0:
		return 1 # ??
	elif x == 1:
		return 2
	else:
		return moveDigit(x - 1) * (x + 1)
		

answer = ''
digits = [str(i) for i in xrange(0, 10)]

cursor = 1
digit = 9
while digit >= 1:
	test = cursor
	i = -1
	while test <= 1000000:
		i += 1
		test += moveDigit(digit - 1)
	
	if i > 0:
		cursor += (moveDigit(digit - 1) * i)
	else:
		i = 0
	
	# drop the appropriate digit in the box
	answer += digits.pop(i)
	digit -= 1
	
answer += digits.pop(0)
print answer