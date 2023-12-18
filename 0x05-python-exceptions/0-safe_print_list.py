#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cpt = 0
    sum = 0
    for cpt in range(x):
        try:
            print("{}".format(my_list[cpt]), end="")
            sum += 1
        except:
            continue
    print()
    return sum
