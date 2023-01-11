#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    A function that returns a set of common elements in two sets

    Parameters
    ----------
    set_1 : first set
    set_2 : second set

    Return:
        A set of common elements
    """
    c_set = set_1 & set_2
    return (c_set)
