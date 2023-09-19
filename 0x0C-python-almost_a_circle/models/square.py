#!/usr/bin/python3

"""


    Class Square which inherits from Rectangle


"""

from .rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of the Square

        Args:
            size: size of the square
            x: x
            y: y
            id: id of attribute
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
               f"{self.width}"
