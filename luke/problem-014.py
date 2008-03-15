#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=12
import math

def seq(x, count = 1):
	if x == 1:
		return count
	elif not x % 2:
		return seq(int(x / 2), count + 1)
	else:
		return seq(int(3 * x + 1), count + 1)
		
cursor = 1000000
highSeqCount = 0
while cursor >= 1:
	seqCount = seq(cursor)
	if seqCount > highSeqCount:
		highSeqCount = seqCount
		answer = cursor
	cursor -= 1
	
print answer