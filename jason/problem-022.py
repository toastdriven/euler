#!/usr/bin/env python

import csv

names = csv.reader(open('names.txt')).next()
names.sort()
count = 1
total = 0
for name in names:
    total += sum(ord(letter) - 64 for letter in name) * count
    count += 1

print total