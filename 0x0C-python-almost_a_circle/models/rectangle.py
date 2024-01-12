#!/usr/bin/python3
'''Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialization with id that inherits.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        '''Getter of Width.'''
        return self.__width

    @property
    def height(self):
        '''Getter of Height.'''
        return self.__height

    @property
    def x(self):
        '''getter of x.'''
        return self.__x

    @property
    def y(self):
        '''getter of y.'''
        return self.__y


    @width.setter
    def width(self, value):
        self.__width = value
 

    @height.setter
    def height(self, value):
        self.__height = value

   
    @x.setter
    def x(self, value):
        self.__x = value

   
    @y.setter
    def y(self, value):
        self.__y = value
