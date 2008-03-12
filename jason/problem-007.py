#!/usr/bin/env python

import math

def isPrime(num):
    halfway = int(math.ceil(math.sqrt(num))) + 1
    for i in range(2, halfway):
        if not num % i:
            return False
    return True

i = 0
count = 1
while count <= 10001:
    i += 1
    if(isPrime(i)):
        count += 1

print i