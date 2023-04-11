#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """define a public instance method that
    raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")
