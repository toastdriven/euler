#!/usr/bin/env python

import math

target = 600851475143

def isPrime(num):
    halfway = int(math.ceil(math.sqrt(num))) + 1
    for i in range(2, halfway):
        if not num % i:
            return False
    return True


halfway = int(math.ceil(math.sqrt(target))) + 1
divisors = [i for i in range(1, halfway) if not target % i]
primes = [divisor for divisor in divisors if isPrime(divisor)]
print max(primes)
