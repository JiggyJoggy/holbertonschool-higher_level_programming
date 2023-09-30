#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Using super to change"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns square info"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Return size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Args to attribute"""
        num_args = len(args)
        if num_args and num_args != 0:
            if num_args >= 1:
                self.id = args[0]
            elif num_args >= 2:
                self.size = args[1]
            elif num_args >= 4:
                self.x = args[2]
            elif num_args >= 5:
                self.y = args[3]
        elif kwargs and kwargs != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
