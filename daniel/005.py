#!/usr/bin/env python
start_at = 1
end_at = 10

def greatest_common_number(start_at, end_at):
    gcn = 1
    
    for i in xrange(start_at, end_at):
        gcn *= i
    
    return gcn

print greatest_common_number(start_at, end_at)