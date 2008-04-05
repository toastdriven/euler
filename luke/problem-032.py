#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=32
solutions = []
for i in xrange(1,100):
	for j in xrange(i, 9876):
		p = i * j
		digits = list(str(p)) + list(str(i)) + list(str(j))
		
		if len(digits) == 9:			
			digits.sort()
			if digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
				solutions.append((i, j, p))

answer = 0
known_products = []
for i in solutions:
	try:
		known_products.index(i[2])
	except ValueError:
		known_products.append(i[2])
		answer += i[2]

print answer