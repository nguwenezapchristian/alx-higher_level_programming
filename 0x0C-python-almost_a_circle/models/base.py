#!/usr/bin/python3

"""


    This is a Base class for all other
    classes in this project.


"""


class Base():
    """ this is the Base class """
    __nb_objects = 0

    @classmethod
    def reset_nb_objects(cls):
        cls.__nb_objects = 0

    def __init__(self, id=None):
        """ contructor for the base class

        Args:
            id: id attribute
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
