#!/usr/bin/python3
''' inherits_from method for task 4.'''

def inherits_from(obj, a_class):
    '''checks if an object is a direct subclass of a parent one and not a class itself.'''
    return isinstance(obj, a_class) and type(obj) != a_class
