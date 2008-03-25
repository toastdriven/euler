#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=22
import csv
from EulerLibs import StrLibs

class customDialect(csv.Dialect):
	delimiter = ','
	doublequote = False
	escapechar = '\\'.
	lineterminator = "\n"
	quotechar = '"'
	quoting = False
	skipinitialspace = False

names_by_line = csv.reader(file('data/names.txt', 'r'), dialect = customDialect)
names = list(names_by_line)[0]
names.sort()

answer = 0
cursor = 0
while cursor < len(names):	
	value = StrLibs.wordValue(names[cursor])
	cursor += 1
	answer += (cursor * value)
			
print answer