#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    outcome = 0
    i = 0

    if type(roman_string) is str and roman_string:
        for ch in range(len(roman_string) - 1, -1, -1):
            if values[roman_string[ch]] >= i:
                outcome += values[roman_string[ch]]
            else:
                outcome -= values[roman_string[ch]]
            i = values[roman_string[ch]]
    return outcome
