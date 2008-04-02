#!/usr/bin/env python

def seq_length(n):
    length = 0
    while n > 1:
        length += 1
        if(n % 2):
            n = (3 * n) + 1
        else:
            n = n / 2
    return length

max_num = 0
max_len = 0
for i in xrange(500000, 1000000):
    length = seq_length(i)
    if length > max_len:
        max_len = length
        max_num = i

print max_num
