#!/usr/bin/env python

from MyMath import *

i = 1
while (len(factors(i)) <= 500):
	i += 1
	answer = triangleNumber(i)
	
print answer