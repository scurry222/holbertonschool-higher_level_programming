#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    total = 0

    for i in range(0, len(text)):
        total += 1

    space = False

    for ch in text:
        if ch is '.' or ch is '?' or ch is ':':
            print("{}\n\n".format(ch), end="")
            space = True
            continue
        if space and ch is ' ':
            continue
        if space and ch is not ' ':
            space = False
        print("{}".format(ch), end="")
