#!/usr/bin/pyethon3

"""


    This unittest for Base class


"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ This a class for Test cases for Base class """

    @classmethod
    def setUpClass(cls):
        """ here i am initializing the __nb_objects
        to zero before starting the test """

        cls.__nb_objects = 0

    def test_id_none(self):
        """ test the value of the id when the instance is created """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = base()
        self.assertEqual(b2.id, 2)

    def test_id_not_none(self):
        """ test the value of id when id is not equal to None """

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

if __name__ == "__main__":
    unittest.main()
