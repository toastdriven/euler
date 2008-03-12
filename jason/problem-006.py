#!/usr/bin/env python

sumOfSquares = sum(i**2 for i in range(1, 101))
squareOfSums = sum(i for i in range(1, 101))**2
print squareOfSums - sumOfSquares