#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    cpt = 0
    counted = 0
    for cpt in range(0, x):
        try:
            print("{:d}".format(my_list[cpt]), end="")
            counted += 1
        except (ValueError, TypeError):
            continue
    print()
    return counted
