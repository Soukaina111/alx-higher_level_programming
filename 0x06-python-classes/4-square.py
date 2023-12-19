#!/usr/bin/python3
""" class Square"""


class Square:
    """ class Square"""
    def __init__(self, size=0):
        """ init square

        Args:
            value (int): square size.
        """
        self.size = size

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.
        Args:
            value (int): square size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """returns the area
        """
        return self.__size**2
