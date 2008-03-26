#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=25
import math

cursor = 1
prev = 1
answer = 2

while len(str(cursor)) < 1000:
	t = cursor
	cursor += prev
	prev = t
	answer += 1
	
print answer