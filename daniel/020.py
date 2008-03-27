#!/usr/bin/env python
from useful_euler import factorial
# starting_number = 6
starting_number = 100
print sum(int(i) for i in str(factorial(starting_number)))