#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=6
import math

sum_of_squares = 0
i = 1
while i <= 100:
	sum_of_squares += int(math.pow(i, 2))
	i += 1
	
sum_only = 0
i = 1
while i <= 100:
	sum_only += i
	i += 1
		
answer = int(math.pow(sum_only, 2) - sum_of_squares)
print answer