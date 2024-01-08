#!/usr/bin/python3
'''BaseGeometry class for task 7.'''


class BaseGeometry:
    '''BaseGeometry class.'''
    def area(self):
        '''Method to calculate the area belonging to this class.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method to validate the value type and content.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
