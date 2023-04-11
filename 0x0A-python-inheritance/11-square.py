#!/usr/bin/python3
"""a class that inherits from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """a class that uses Rectangle"""
    def __init__(self, size):
        """initializing the new class
        Args:
            size(int): the new size of the square"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """prints the square"""
        return "[Square] {} / {}".format(self.__size, self.__size)
