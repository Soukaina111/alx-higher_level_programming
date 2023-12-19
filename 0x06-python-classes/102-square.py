#!/usr/bin/python3
""" defines a square"""


class Square:
    """ class Square"""
    def __init__(self, size=0):
        """ init square
        Args:
            value (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): square size.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """returns the area
        """
        return self.__size**2

    def __lt__(self, oth):
        return self.size < oth.size

    def __le__(self, oth):
        return self.size <= oth.size

    def __eq__(self, oth):
        return self.size == oth.size

    def __ne__(self, oth):
        return self.size != oth.size

    def __ge__(self, oth):
        return self.size >= oth.size
