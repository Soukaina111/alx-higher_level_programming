#!/usr/bin/python3
'''Square class Module.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization of attributes.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns data of the square as a string.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''square's size.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''update attributes method.'''
        if id != None:
            self.id = id
        if size != None:
            self.size = size
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates  no-keyword & keyword args instances.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary format of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
