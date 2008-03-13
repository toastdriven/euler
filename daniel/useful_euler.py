"""A library for working with Project Euler problems."""
import math

def is_prime(number):
    """Determines if a number is prime or not."""
    for i in range(2, int(math.ceil(math.sqrt(number)))):
        if number % i == 0.0:
            return False

    return True

def fib(prev, current):
    """
    Provides a generator for Fibanocci numbers.
    
    Usually started with Math.fib(0, 1).
    """
    while True:
        (prev, current) = (current, prev + current)
        yield prev

def sieve(max_number):
    """Returns all primes up to a maximum number."""
    full_set = range(0, max_number + 1)
    full_set[0:2] = (None, None)
    
    for i in xrange(2, max_number + 1):
        for remove_me in xrange(i * 2, max_number + 1, i):
            full_set[remove_me] = None
    
    return [i for i in full_set if i]

def is_palindrome(string, case_insensitive=False):
    """Determines if the string is a palindrome."""
    if case_insensitive:
        string = string.lower()
    
    half_length = int(math.floor(len(string) / 2))
    first = string[0:half_length]
    last = string[(len(string) - half_length):]
    return first == last[::-1]