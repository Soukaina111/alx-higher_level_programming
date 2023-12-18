#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    counted = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            counted += 1
        except:
            continue
    print()
    return counted
