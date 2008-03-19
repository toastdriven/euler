#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=15
import math, copy

def get_permutations(size, hops = []):
	result = 0
	directions = (0, 1)
	
	if len(hops) == int(size * 2):
		result += 1
	else:
		for i in directions:
			if hops.count(i) < int(size):
				result += get_permutations(size, hops + [i])
			
	return result
	

answer = get_permutations(20)
print answer