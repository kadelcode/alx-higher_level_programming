#!/usr/bin/python3

for n1 in range(0, 10):
    for n2 in range(1, 10):
        if n2 > n1:
            print("{}{}".format(n1, n2), end='')
            if int(str(n1) + str(n2)) != 89:
                print(end=', ')
print()
