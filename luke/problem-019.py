#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=19
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
days_in_month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# the first sunday of the 20th century
year = 1901
month = 1
day = 6

sunday_the_firsts = 0
while year <= 2000:
	# check for leap year and address appropriately
	if (not year % 4) and (year % 100 or not year % 400):
		days_in_month[2] = 29
	else:
		days_in_month[2] = 28
	
	while month <= 12:
		while day <= days_in_month[month]:
			if day == 1:
				sunday_the_firsts += 1
				
			day += 7
		
		# reset the day cursor for the next month
		day = day - days_in_month[month]		
		month += 1
	
	# reset the month cursor for the next year
	month = 1
	year += 1
	
print sunday_the_firsts