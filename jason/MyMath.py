#!/usr/bin/env python
import operator

def primes(n):
    """Returns the primes up to n."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n**0.5)+1):
        if sieve[i]:
            for j in xrange(i**2, n, i):
                sieve[j] = 0
    return [p for p in sieve if p]


def isPrime(num):
    """Determines if a number isPrime."""
    for i in xrange(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True

def triangleNumber(n):
    """Returns the nth triangle number."""
    return (n * (n + 1)) / 2

def factors(num):
    """Determine the factors of a number."""
    factors = []

    if num == 1:
        factors.append(1)
        return factors

    for i in xrange(1, int(num**0.5)+1):
        if not num % i:
            factors.append(i)
            if(i != num/ i):
                factors.append(num / i)

    return factors

def divisors(num):
    """Determine the integer divisors for a number."""
    divs = factors(num)
    divs.remove(num)
    return divs

def fact(num):
    """ Returns a number's factorial."""
    return reduce(operator.mul, xrange(2, num + 1))

def isAbundant(num):
    return sum(divisors(num)) > num

def abundants(num):
    """Returns a list of abundant numbes less than num."""
    if num >= 12:
        return [i for i in xrange(12, num + 1) if isAbundant(i)]
    else:
        return []
