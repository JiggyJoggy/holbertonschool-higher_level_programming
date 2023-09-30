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
