#!/usr/bin/env python

palindrones = []

for x in range(100, 1000):
    for y in range(100, 1000):
        product = str(x * y)
        if(product == product[::-1]):
            palindrones.append(x * y)

print max(palindrones)
