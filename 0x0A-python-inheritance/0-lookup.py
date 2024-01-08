#!/usr/bin/python3
'''lookup method  for first task.'''


def lookup(obj):
    '''Looks for instances and methods f an object.
    Args:
        obj (object): the object to list its details.

    Returns:
        list: the list of details.
    '''
    return dir(obj)
