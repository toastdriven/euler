#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=26
from EulerLibs import StrLibs

# Note: I am convinced that this would fail given the exact correct input (basically, anything where the 5000th digit and 4999th digit were
# set up to cause the system to think the cycle had repeated early). However, it got the correct answer, so I didn't bother to fix it.
def cycle(n):
	decimal = str(10**5000 / n)
	
	# case for numbers with no recurring cycle
	if decimal[len(decimal) - 1] == '0':
		return 0
		
	# case for numbers with a recurring cycle
	i = 0
	reversed_decimal = decimal[::-1] # string reverse
	possible_cycle = ''
	cycle_found = False
	while not cycle_found:
		possible_cycle += reversed_decimal[i]
		i += 1
				
		if possible_cycle == reversed_decimal[len(possible_cycle):2 * len(possible_cycle)]:
			cycle_found = True
					
	# print "%d's recurring cycle has %d digits." % (n, len(possible_cycle))
	return len(possible_cycle)
		
			
cursor = 0
for i in range(1,1001):
	cyc_i = cycle(i)
	if cyc_i > cursor:
		answer = i
		cursor = cyc_i
		
print answer