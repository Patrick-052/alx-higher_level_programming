#!/usr/bin/python3
"""defines a square class that inherits from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Represent asquare using Rectangle"""
    def __init__(self, size):
        """initializing a new square.
        Args:
            size (int): the new size of the square"""
        super().__init__()
        self.integer_iterator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
