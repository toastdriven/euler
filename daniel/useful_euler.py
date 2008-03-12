"""A library for working with Project Euler problems."""
import math


class PEMath(object):
    """Provides useful mathematical methods."""
    @classmethod
    def is_prime(cls, number):
        """Determines if a number is prime or not."""
        for i in range(2, int(math.ceil(math.sqrt(number)))):
            if number % i == 0.0:
                return False
    
        return True
    
    @classmethod
    def fib(cls, prev, current):
        """
        Provides a generator for Fibanocci numbers.
        
        Usually started with Math.fib(0, 1).
        """
        while True:
            (prev, current) = (current, prev + current)
            yield prev


class PEString(object):
    """Provides useful string methods."""
    @classmethod
    def is_palindrome(cls, string, case_insensitive=False):
        """Determines if the string is a palindrome."""
        if case_insensitive:
            string = string.lower()
        
        half_length = int(math.floor(len(string) / 2))
        first = string[0:half_length]
        last = string[(len(string) - half_length):]
        return first == last[::-1]