#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for elem in my_string:
        if elem != "c" and elem != "C":
            new += elem
    return (new)
