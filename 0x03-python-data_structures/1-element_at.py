#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < int(0):
        return None
    elif idx > int(len(my_list)):
        return None
    else:
        return my_list[idx]
