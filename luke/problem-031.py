#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=31
def getCombos(n, coins = [200, 100, 50, 20, 10, 5, 2, 1]):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	
	cursor = 0	
	for i in coins:
		cursor += getCombos(n - i, coins[coins.index(i):len(coins)])
		
	return cursor
		
print getCombos(200)