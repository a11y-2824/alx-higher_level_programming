#!/usr/bin/python3


''' define the protoptype

a and b are integers or floats

'''


def add_integer(a, b=98):
    ''' raise TypeError exception
    include a messge with the error
    '''
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    ''' return the value'''
    return (int(a)+int(b))
