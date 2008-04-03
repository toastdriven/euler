#!/usr/bin/env python

from MyMath import *

abundant_dict = dict(((a, True) for a in abundants(28124)))

def isAbundantSum(num):
    #trim the list down to the number
    for a in abundant_dict:
        if a >= num:
            return False
        if abundant_dict.has_key(num - a):
                return True
    return False

print sum(i for i in xrange(1, 28124) if not isAbundantSum(i))
