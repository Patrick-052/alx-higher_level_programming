#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for y in range(len(my_list)):
        if my_list[y] % 2 == 0:
            return True
    return False
