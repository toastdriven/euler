#!/usr/bin/env python

import datetime

count = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:
            count += 1
            
print count