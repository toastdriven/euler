#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=29
def power_sequence(minimum, maximum):
	seq = []
	for a in xrange(minimum, maximum + 1):
		for b in xrange(minimum, maximum + 1):
			try:
				seq.index(a**b)
			except ValueError:
				seq.append(a**b)
				
			try:
				seq.index(b**a)
			except ValueError:
				seq.append(b**a)
		
	seq.sort()		
	return seq

answer = len(power_sequence(2, 100))
print answer