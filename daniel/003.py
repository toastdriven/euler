#!/usr/bin/env python
import math

def is_prime(number):
    for i in range(2, int(math.ceil(math.sqrt(number)))):
        if number % i == 0.0:
            return False
    
    return True

# source_number = 13195
source_number = 600851475143
largest_prime = 0
current = int(math.ceil(math.sqrt(source_number)))
end_at = 2

while current > end_at:
    if source_number % current == 0.0:
        if is_prime(current):
            largest_prime = current
            break
    current -= 1

print "The largest prime is: %s" % largest_prime