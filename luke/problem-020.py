#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=20
import math
from EulerLibs import MathLibs,StrLibs

f100 = str(MathLibs.factorial(100))
answer = StrLibs.sumDigits(f100)
print answer