#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        A = a / b
    except:
        A = None
    finally:
        print("Inside result: {}".format(A))
    return A
