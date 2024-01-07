#!/usr/bin/python3
"""Module for add_integer Method."""


def add_integer(a, b=98):
    """Adds two ints.

    Arguments:
        a: the first int.
        b: the second int, set as 98 by default.

    Raises:
        TypeError: if a or b are not integers or float.

    Returns:
        The total of  a and b after casting them as integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
