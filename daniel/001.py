#!/usr/bin/env python
the_sum = 0

for i in range(1, 1000):
    if not i % 3 or not i % 5:
        the_sum += i

print "The answer: %s" % the_sum