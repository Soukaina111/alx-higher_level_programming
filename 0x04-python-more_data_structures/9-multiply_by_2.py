#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic2 = a_dictionary.copy()
    list_keys = list(dic2.keys())

    for i in list_keys:
        dic2[i] *= 2

    return (dic2)
