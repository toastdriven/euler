#!/usr/bin/env python
answer = 0
for i in range(1,1000):
	if i % 3 or i % 5:
		answer += i

print answer