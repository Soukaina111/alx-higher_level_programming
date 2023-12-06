#!/usr/bin/python3
def uniq_add(my_list=[]):
     unique_integers = set()
    total = 0

    for num in my_list:
        if num not in unique_integers:
            total += num
            unique_integers.add(num)

    return total
