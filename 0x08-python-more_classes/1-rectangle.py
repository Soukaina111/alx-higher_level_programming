#!/usr/bin/python3
"""Defines Rectangle Class"""


class Rectangle:
    """
    Class defining properties of rectangle.

    Attributes of the shape:
        width (int)
        height (int)
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional):equals to 0 by default.
            height (int, optional):equals to 0 by default.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get the width.

        Returns:
            the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """ gets Height .

        Returns:
          the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Raises Errors in case:
            width is not an integer or less than 0.
           
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """To update the height.

        Raises Errors in case:
           height is not an integer or less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
