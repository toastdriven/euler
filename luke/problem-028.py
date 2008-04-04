#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=28
def spiral_sum(n):
	# edge case
	if n == 1:
		return 1
		
	jump = n - 1
	return spiral_sum(n - 2) + reduce(lambda x, y: x + y, xrange((n - 2)**2 + jump, (n - 2)**2 + (jump * 4) + 1, jump))
	
print spiral_sum(1001)