#!/usr/bin/python3
'''Rectangle Module'''
from models.base import Base


class Rectangle(Base):
    '''Class representation of Rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializer.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Parameter of width rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_inte("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Parameter of height rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_inte("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''argument x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_inte("x", value)
        self.__x = value

    @property
    def y(self):
        '''argument y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_inte("y", value)
        self.__y = value

    def validate_inte(self, name, value, eq=True):
        '''Method to validate the value integer.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Calculate the area .'''
        return self.width * self.height

    def display(self):
        '''Shows string format of this rectangle.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns string data.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Method updating attributes .'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updating attributes .'''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary format of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
