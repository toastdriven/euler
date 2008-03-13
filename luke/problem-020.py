#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=20
import math
from EulerLibs import MathLibs,StrLibs

pf100 = str(MathLibs.pfactorial(100))
answer = StrLibs.sumDigits(pf100)
print answer