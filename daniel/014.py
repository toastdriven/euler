#!/usr/bin/env python
def the_rules(number):
    if number % 2 == 0:
        return number / 2
    else:
        return (3 * number) + 1

def generate_chain(current_number):
    count = 1
    
    while current_number != 1:
        current_number = the_rules(current_number)
        count += 1
    
    return count

# print generate_chain(13)
# exit()

number_with_longest_chain = 0
longest_chain = 0

for i in xrange(1, 1000000):
    chain_length = generate_chain(i)
    
    if chain_length > longest_chain:
        number_with_greatest_chain = i
        longest_chain = chain_length

print "Number with longest chain: %s" % number_with_greatest_chain