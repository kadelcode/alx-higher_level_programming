#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_in_one = (set_1 | set_2) - (set_1 & set_2)
    return (c_in_one)
