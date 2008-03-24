#!/usr/bin/env python
from useful_euler import triangle_number, factors

# for i in xrange(1, 8):
#     print factors(triangle_number(i))

def factors_for_triangle(number):
    return factors(triangle_number(number))

current_number = 1
current_length = len(factors_for_triangle(current_number))

while current_length <= 500:
    current_number += 1
    current_length = len(factors_for_triangle(current_number))

print "The triangle number with > 500 divisors: %s" % triangle_number(current_number)