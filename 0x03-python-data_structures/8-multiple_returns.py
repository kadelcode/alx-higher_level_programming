#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == '':
        first = None
    else:
        first = sentence[0]
    multiple_tuple = (length, first)

    return (multiple_tuple)
