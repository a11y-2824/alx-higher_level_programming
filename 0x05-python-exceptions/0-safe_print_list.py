#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    print(''.join((map(str, my_list[:x]))))
    return (x)
    try:
        safe_print_list()
    except IndexError:
        exit()
