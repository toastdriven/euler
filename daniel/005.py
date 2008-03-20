#!/usr/bin/env python
def factorial(num):
    if num == 1:
        return 1
    
    return num * factorial(num - 1)

def check_divisible(total, current_number):
    if current_number <= 1:
        return True
    
    if total % current_number == 0:
        return check_divisible(total, current_number - 1)
    else:
        return False

# max_num = 10
max_num = 20
start_at = sum(xrange(1, max_num + 1))
end_at = factorial(max_num)
smallest_evenly_divisible = 0
current = start_at

# for i in xrange(start_at, end_at):
while current <= end_at:
    if check_divisible(current, max_num):
        smallest_evenly_divisible = current
        break
    
    current += 1

print "Smallest Evenly Divisible: %s" % smallest_evenly_divisible