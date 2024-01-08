#!/usr/bin/python3
'''Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''rectangle child class.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method to compute area of square.'''
        return self.__size ** 2

    def __str__(self):
        '''Returns  square as string.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
