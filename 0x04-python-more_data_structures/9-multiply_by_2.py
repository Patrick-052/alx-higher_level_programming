#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for k, v in a_dictionary.items():
        new_value = (v*2)
        new_dictionary[k] = new_value
    return new_dictionary
