#!/usr/bin/python3
"""defines a class square"""
class square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
