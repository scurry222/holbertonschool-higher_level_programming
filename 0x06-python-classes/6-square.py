#!/usr/bin/python3
class Square:
    """ A class that defines a square

    Attributes:
        size (obj: 'int'): size of the square
        area (obj: 'int'): area of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes square class

        Args:
            size (obj: 'int'): for size attribute
            position (obj: 'int') for position attribute
        """
        self.__size = size
        self.__position = position
        """ Set private attribute of square size to var size
            Set private attribute of position to var position
        """

    @property
    def size(self):
        """ Defines size of square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Defines size of square object to change to value

        Args:
            size (obj:'int') size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """ Only positive integers allowed for attribute size

        """
        self.__size = value

    @property
    def position(self):
        """ Defines position of square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets position of value if its a tupe of 2 pos ints

        """
        if type(value) is not tuple or len(value) is not 2 or\
           type(value[0]) is not int or value[0] < 0 or\
           value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Defines area of square object

        """
        return self.__size ** 2

    def my_print(self):
        """ Prints a square of hashes

        """
        if self.__size is 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print((" " * self.__position[0]) + ('#' * self.__size))


