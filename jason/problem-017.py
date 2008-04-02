#!/usr/bin/env python

number_words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def number_length(n):
    if n < 20:
        return len(number_words[n])
    if n < 100:
        if n % 10 == 0:
            return len(number_words[n])
        else:
            return number_length(n - n % 10) + number_length(n % 10)
    if n < 1000:
        if n % 100 == 0:
            return number_length(n / 100) + len('hundred')
        else:
            return number_length(n - n % 100) + len('and') + number_length(n % 100)
    if n == 1000:
        return len('onethousand')
    
print sum(number_length(i) for i in xrange(1, 1001))