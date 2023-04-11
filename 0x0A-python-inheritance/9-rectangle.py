#!/usr/bin/python3
"""a class that inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """the class representation"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
    print("[Rectangle] {} / {}".format(self.__width, self.__height))
