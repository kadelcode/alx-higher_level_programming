#!/usr/bin/python3
""" A function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """Appends a string """
    with open(filename, "a", encoding="utf-8") as f:
        append_text = f.write(text)

    return append_text
