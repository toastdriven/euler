#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=2
precursor = 1
cursor = 1
answer = 0
while cursor <= 4000000:
	# move the precursor and the cursor to the next
	# number in the fibonacci sequence
	(precursor, cursor) = (cursor, cursor + precursor)
	
	# if the cursor is a number that is even, add it
	# to the final answer
	if cursor % 2:
		answer += cursor
		
print answer