#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer.
    """
    from functools import reduce
    roman = list(roman_string)
    for c in range(len(roman)):
        if roman[c] == 'M':
            roman[c] = 1000
        elif roman[c] == 'C':
            roman[c] = 100
        elif roman[c] == 'D':
            roman[c] = 500
        elif roman[c] == 'L':
            roman[c] = 50
        elif roman[c] == 'X':
            roman[c] = 10
        elif roman[c] == 'V':
            roman[c] = 5
        elif roman[c] == 'I':
            roman[c] = 1

    return reduce(lambda x, y: y + x if x > y else y - x, roman)
