#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=15
import math, copy
from EulerLibs import MathLibs

def get_permutations(size, hops = []):
	"""This method will calculate the permutations correctly, but takes too long."""
	result = 0
	directions = ('right', 'down')
	
	if len(hops) == int(size * 2):
		return 1
	else:
		return sum([get_permutations(size, hops + [i]) for i in directions if hops.count(i) < int(size)])
		
def get_permutations_faster(size):
	"""The fast version of get_permutations (ascertained by pattern matching to the slow one)."""
	if size == 2:
		return 6
	else:
		result = 0
		result += get_permutations_faster(size - 1)
		# sets beginning with the same movement (right or down) twice are ((size - 1) / size) as large as the sets acquired above		
		result *= (2 * size - 1)
		result /= size
		result *= 2
		return result
		
answer = get_permutations_faster(20)
print answer