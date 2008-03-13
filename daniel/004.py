#!/usr/bin/env python
from useful_euler import is_palindrome

largest_product, largest_left, largest_right = 0, 0, 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        
        if product > largest_product:
            if is_palindrome(str(product)):
                largest_product = product
                largest_left, largest_right = i, j

print "The largest palindrome is %s (%s x %s)." % (largest_left * largest_right, largest_left, largest_right)