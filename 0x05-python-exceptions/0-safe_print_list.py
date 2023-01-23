#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print(my_list[i], end='')
        print()

    except IndexError:
        print()
        print("Length of list exceeded!")
        raise

    return (x)
