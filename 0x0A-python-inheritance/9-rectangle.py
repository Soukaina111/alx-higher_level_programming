#!/usr/bin/python3
'''Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A childclass named a rectangle.'''
    def __init__(self, width, height):
        '''Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method returning rectangle's area.'''
        return self.__width * self.__height

    def __str__(self):
        '''method to reprensent string.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
