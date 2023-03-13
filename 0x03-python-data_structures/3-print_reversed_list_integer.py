#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for element in my_list:
        my_list.reverse(element)
        if isinstance(element, int):
            print("{:d}".format(my_list.reverse(element)))
