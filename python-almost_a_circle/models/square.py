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
        if args:
            arg_names = ['id', 'size', 'x', 'y']
            for index, arg in enumerate(args):
                setattr(self, arg_names[index], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
