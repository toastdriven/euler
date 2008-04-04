#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=30
def digitPowerSum(n):
	digit_powers = [i**5 for i in xrange(0, 10)]	
	return reduce(lambda x, y: x + digit_powers[int(y)], [0] + list(str(n)))
	
print sum([i for i in xrange(10,1000000) if i == digitPowerSum(i)])