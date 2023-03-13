#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for element in my_list:
        if isinstance(element, int):
            my_list.reverse(element)
            print("{:d}".format(my_list.reverse(element)))
