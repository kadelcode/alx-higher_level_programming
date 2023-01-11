#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dic = list(a_dictionary)  # convert the dictionary to a list of keys

    sort_list = sorted(list_dic)

    for i in sort_list:
        print("{}: {}".format(i, a_dictionary[i]))
