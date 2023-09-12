#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
            'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900}
    index = 0
    number = 0
    while index < len(roman_string):
        if index + 1 < len(roman_string) and roman_string[index:index + 2] in roman:
            number += roman[roman_string[index:index + 2]]
            index += 2
        else:
            number += roman[roman_string[index]]
            index++
    return number
