#!/usr/bin/env python
word_mapping = {
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
    100: 'one hundred',
    200: 'two hundred',
    300: 'three hundred',
    400: 'four hundred',
    500: 'five hundred',
    600: 'six hundred',
    700: 'seven hundred',
    800: 'eight hundred',
    900: 'nine hundred',
    1000: 'one thousand',
}

def translate_number_to_words(number):
    if number in word_mapping:
        return word_mapping[number]
    
    available_numbers = word_mapping.keys()
    available_numbers.sort()
    available_numbers.reverse()
    words = []
    
    while number > 0:
        for i in available_numbers:
            if number >= i:
                words.append(word_mapping[i])
                number -= i
                
                if i >= 100 and number < 100:
                    words.append('and')
    
    return words

# print translate_number_to_words(200)
# exit()

big_string = ''

for i in xrange(1, 1001):
    words = translate_number_to_words(i)
    big_string += ''.join(words)

big_string = big_string.replace(' ', '')
print "Length of all letters: %s" % len(big_string)