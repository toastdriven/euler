#!/usr/bin/env python

from MyMath import factors

total = 0
for a in xrange(2, 10000):
    b = sum(factors(a)) - a
    if a != b and a == sum(factors(b)) - b:
        total += a
        
print total