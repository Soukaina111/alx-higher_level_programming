#!/usr/bin/python3
def to_subtract(list_num):
    to_sub = 0
    list2 = max(list_num)

    for n in list_num:
        if list2 > n:
            to_sub += n

    return (list2 - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_nunmbers.keys())

    n = 0
    last_rom = 0
    list_n = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    n += to_subtract(list_n)
                    list_n = [rom_n.get(ch)]
                else:
                    list_n.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    n += to_subtract(list_n)

    return (n)
