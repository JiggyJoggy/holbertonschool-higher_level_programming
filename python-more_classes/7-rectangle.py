#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of properties"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getting width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting values"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getting height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Getting area"""
        return self.__height * self.__width

    def perimeter(self):
        """Getting perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Return a string of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                rectangle_str += str(self.print_symbol)
            rectangle_str += "\n"
        return rectangle_str[:-1]

    def __print__(self):
        """Prints rectangle"""
        print(self)

    def __repr__(self):
        """Returns a string that can be used again
        with a new instance using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when instance is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
