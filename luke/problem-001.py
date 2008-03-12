#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=1
answer = 0
for i in range(1,1000):
	if i % 3 or i % 5:
		answer += i

print answer