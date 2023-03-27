#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i], end=""))
            counter += 1
    except IndexError:
        print("Index does not exist")
    except TypeError:
        print("wrong type")
    return counter
