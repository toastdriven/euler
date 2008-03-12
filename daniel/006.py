#!/usr/bin/env python
start_at = 1
end_at = 101

sum_of_squares = sum(i*i for i in range(start_at, end_at))
square_of_sums = sum(i for i in range(start_at, end_at))
square_of_sums *= square_of_sums
the_difference = square_of_sums - sum_of_squares

print "The difference: %s" % the_difference