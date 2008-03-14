#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=17
import math
from EulerLibs import MathLibs

def strOfNum(x):
	x = list(str(x))
	x.reverse()
	x = ''.join(x)

	s = ''
	i = 1
	while i < 10**len(x):
		skip_tens = False
		
		# ones place
		if i == 1:
			if len(x) > 1 and int(x[1]) == 1:
				text = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
				skip_tens = True
			else:
				text = ['','one','two','three','four','five','six','seven','eight','nine']
		# tens place
		elif i == 10:
			text = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
		# hundreds place
		elif i == 100:
			if int(x[0]) == 0 and int(x[1]) == 0:
				text = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']
			else:
				text = ['', 'one hundred and', 'two hundred and', 'three hundred and', 'four hundred and', 'five hundred and', 'six hundred and', 'seven hundred and', 'eight hundred and', 'nine hundred and']
		# thousands place
		elif i == 1000:
			text = ['', 'one thousand']
			
		s = text[int(x[int(math.log10(i))])] + s
		
		if skip_tens:
			i *= 100
		else:
			i *= 10
		
	return s
	
s = ''
for i in range(1,1001):
	s += strOfNum(i)
s = s.replace(' ', '')
	
print s	

answer = len(s)
print answer