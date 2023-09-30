#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return width"""
        return self.__wdith

    @width.setter
    def width(self, width):
        """Setting width"""
        self.__width = width

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setting height"""
        self.__height = height

    @property
    def x(self):
        """Return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setting x"""
        self.__x = x

    @property
    def y(self):
        """Return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setting y"""
        self.__y = y
