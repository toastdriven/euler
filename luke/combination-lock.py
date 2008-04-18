#!/usr/bin/env python
def count_permutations(available_presses):
	cursor = 0
	
	# base case
	if not len(available_presses):
		return 0
	
	# iterate through each possible button or combination
	# of buttons to be pressed
	for i in available_presses:
		# find all remaining acceptable combinations
		remaining_presses = [j for j in available_presses if i & j == 0]
		
		# return the value of the remaining presses, plus one because we could
		# stop at this point also
		cursor += count_permutations(remaining_presses) + 1
		
	return cursor

answer = count_permutations(range(1,32))
print answer