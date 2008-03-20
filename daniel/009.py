#!/usr/bin/env python
def find_pythagorean(the_sum):
    for c in xrange(1, the_sum):
        for b in xrange(1, c):
            for a in xrange(1, b):
                if a + b + c == the_sum:
                    # print "Sum condition met: %s + %s + %s = %s" % (a, b, c, the_sum)
                    if a ** 2 + b ** 2 == c ** 2:
                        # print "Square condition met!"
                        return (a, b, c)
    return (0, 0, 0)

# the_sum = 12
the_sum = 1000
(a, b, c) = find_pythagorean(the_sum)
print "%s + %s + %s = %s" % (a, b, c, the_sum)
print "Product: %s" % (a * b * c)