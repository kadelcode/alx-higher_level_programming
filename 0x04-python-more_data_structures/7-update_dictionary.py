#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[str(key)] = value
    if key not in a_dictionary:
        a_dictionary[str(key)] = value

    return(a_dictionary)
