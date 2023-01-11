#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        a_dictionary[i] = 2 * a_dictionary[i]
    new_dict = a_dictionary
    return (new_dict)
