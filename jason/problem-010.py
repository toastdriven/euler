#!/usr/bin/env python

length = 2000000
list = range(length + 1)

list[1] = 0
for i in xrange(2, length + 1):
    if list[i] <> 0:
        for x in xrange(i * 2, length + 1, i):
            list[x] = 0

print sum(list)
