#!/usr/bin/env python

sum = 0;
for num in [i for i in range(1000) if not i % 3 or not i % 5] :
    sum += num
print sum