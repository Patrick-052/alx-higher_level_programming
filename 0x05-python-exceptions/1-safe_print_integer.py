#!/usr/bin/python3
def safe_print_integer(value):
    try:
         if isinstance(value, int) and value % 2 == 0:
             print("{:d}".format(value))
    except TypeError:
        return False
    else:
        return True
