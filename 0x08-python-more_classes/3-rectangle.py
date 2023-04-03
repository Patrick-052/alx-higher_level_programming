#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Initialization of the attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

     """Retrieving the width"""
    @property
    def width(self):
        return self.__width
    
    """Setting the width"""
    @width.setter
    def width(self, value):
        """Raise error if present"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer");
        if value < 0:
            raise ValueError("width must be >= 0");
        self.__width = value
        
    """Retrieving the height"""
    @property
    def height(self):
        return self.__height
    
    """Setting the height"""
    @height.setter
    def height(self, value):
        """Raise error if present"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer");
        if value < 0:
            raise ValueError("height must be >= 0");
        self.__height = value

    """method that returns rectangle's area"""
    def area(self):
        return self.__width * self.__height

    """method that returns rectangle's perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
        
    """method that returns rectangle as a string"""
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "Rectangle(width={}, height={})".format(self.width, self.height)
