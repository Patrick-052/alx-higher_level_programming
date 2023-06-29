#!/usr/bin/python3
"""Function to obtain the peak/greatest value
   in a sequence of integers"""


def find_peak(list_of_integers):
    gret = sorted(list_of_integers)
    return (gret[-1])
