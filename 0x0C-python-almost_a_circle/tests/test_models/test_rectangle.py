#!/usr/bin/python3

"""


    Unittest for the class Rectangle


"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ this is the class test for implemmenting
    unittest for class Rectangle
    """

    def test_isinstance(self):
        """ test if the object created an instance of
        the Rectangle class
        """
        
        rect = Rectangle(10, 5, 0, 0, 15)
        self.assertIsInstance(rect, Rectangle, msg=None)

    def test_id_rect(self):
        """ test the id attr of the rectangle instance """

        r1= Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(5, 10)
        self.assertEqual(r2.id, 2)

    def test_id_not_none(self):
        """ test when the id=None """

        r3 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_absent_args(self):
        """ test if no arguments passed """

        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """ chech if only one argument passed """

        with self.assertRaises(TypeError):
            Rectangle(7)

    def test_two_args(self):
        """ when two args are passed, other attribute
        like x and y must be zero and id attr must not be zero
        """
        r5 = Rectangle(2, 10)
        self.assertEqual(r5.width, 2)

    def test_non_int(self):
        """ test if an arg. is non int """

        with self.assertRaises(TypeError):
            Rectangle('5', 7)
        
        with self.assertRaises(TypeError):
            Rectangle(2, 5, 4, '10')

    def test_float(self):
        """Test float width or height."""
        with self.assertRaises(TypeError):
            Rectangle(2.3, 4, 4)

        with self.assertRaises(TypeError):
            Rectangle(2, 3.5, 5)

    def test_negative_args(self):
        with self.assertRaises(TypeError):
            Rectangle(3, -4, 40)

        with self.assertRaises(TypeError):
            Rectangle(-3, 4, 4)

        with self.assertRaises(TypeError):
            Rectangle(2, 4, -4)

    def test_args_overflow(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 0, 0, 10, 11)

    def test_width_getter(self):
        """ test width getter """
        r = Rectangle(4, 10)
        self.assertEqual(r.width, 4)

    def test_height_getter(self):
        """ test width getter """
        r = Rectangle(4, 10)
        self.assertEqual(r.height, 10)

    def test_y_setter(self):
        """ test width getter """
        r = Rectangle(4, 10)
        r.y = 10
        self.assertEqual(r.y, 10)

    def test_x_getter(self):
        """ test width getter """
        r = Rectangle(4, 10)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_area(self):
        """ test the result of area method """
        r10 = Rectangle(3, 2)
        self.assertEqual(r10.area(), 6)

        r11 = Rectangle(2, 10)
        self.assertEqual(r11.area(), 20)

if __name__ == "__main__":
    unittest.main()
