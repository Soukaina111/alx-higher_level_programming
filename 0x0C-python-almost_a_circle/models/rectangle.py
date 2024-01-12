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
        self.validate_intgr("width", value, False)
        self.__width = value
 

    @height.setter
    def height(self, value):
        self.validate_intgr("height", value, False)
        self.__height = value

   
    @x.setter
    def x(self, value):
        self.validate_intgr("x", value)
        self.__x = value

   
    @y.setter
    def y(self, value):
        self.validate_intgr("y", value)
        self.__y = value

    def validate_intgr(self, name, value, eq=True):
        '''validating the value method.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Calculates the area of this rectangle.'''
        return self.width * self.height

    def display(self):
        '''displays the string format of this rectangle.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns string data of this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''update method.'''
        if id != None:
            self.id = id
        if width != None:
            self.width = width
        if height !=  None:
            self.height = height
        if x !=  None:
            self.x = x
        if y != None:
            self.y = y

     def update(self, *args, **kwargs):
        '''Method to update instance  no-keyword & keyword args attributes.'''
        # displays(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''shows dictionary format of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
