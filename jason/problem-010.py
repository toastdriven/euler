#!/usr/bin/env python

import math

primes = []

def isPrime(num):
    for prime in primes:
        if not num % prime:
            return False
    primes.append(num)
    return True


print sum((i for i in xrange(2, 2000000) if isPrime(i)))