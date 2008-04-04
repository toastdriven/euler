#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=31
def getCombos(n, coins = [200, 100, 50, 20, 10, 5, 2, 1]):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	
	return reduce(lambda x, y: x + y, [0] + [getCombos(n - i, coins[coins.index(i):len(coins)]) for i in coins])
			
print getCombos(200)