#!/usr/bin/python3
""" class Square"""


class Square:
    """ class Square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): square size
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        """method area """
    def area(self):
        """returns the area.
        """
        return self.__size**2
