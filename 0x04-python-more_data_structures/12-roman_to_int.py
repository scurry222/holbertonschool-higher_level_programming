#!/usr/bin/python3
def roman_to_int(roman_string):
    base_10 = 0
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return 0
    for index, char in enumerate(roman_string):
        if char not in convert:
            return 0
        elif convert[char] >= convert[roman_string[index]]:
            base_10 += convert[char]
        else:
            base_10 -= convert[char]
    return base_10
