#!/usr/bin/python3
"""
Script/Function for task 6 about Peak
"""
def find_peak(list_of_integers):
    def case_0():
        return None

    def case_1():
        return list_of_integers[0]

    def case_2():
        return max(list_of_integers)

    def case_default():
        mid = len(list_of_integers) // 2
        peak = list_of_integers[mid]

        if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
            return peak
        elif peak < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
        else:
            return find_peak(list_of_integers[mid + 1:])

    switch = {
        0: case_0,
        1: case_1,
        2: case_2,
    }

    switch_case = switch.get(len(list_of_integers), case_default)
    return switch_case()
