#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(c, chr(c - 33)), end="")
