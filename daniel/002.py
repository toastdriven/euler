#!/usr/bin/env python
from useful_euler import fib

f = fib(1, 1)
the_sum, current = 0, 0

while current <= 4000000:
    current = f.next()
    print "%s " % current,
    
    if current % 2 == 0:
        the_sum += current

print
print "The answer: %s" % the_sum