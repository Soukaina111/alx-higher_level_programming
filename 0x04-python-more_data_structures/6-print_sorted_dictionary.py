#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord1 = list(a_dictionary.keys())
    ord1.sort()
    for i in ord1:
        print("{}: {}".format(i, a_dictionary.get(i)))
