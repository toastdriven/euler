#!/usr/bin/env python

sum = 0
(two_back, one_back) = (0, 1)

while one_back <= 4000000 :
    if not one_back % 2:
        sum += one_back
    (two_back, one_back) = (one_back, one_back + two_back)

print sum