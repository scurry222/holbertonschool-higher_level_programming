#!/usr/bin/python3
"""
1-my_list : 1 class

"""


class MyList(list):
    """ Inherit list from MyList """

    def print_sorted(self):
        """ Print list ascending """
        ml = self[:]
        ml.sort()
        print("{}".format(ml))
