import unittest
from inheritance import Rectangle, Circle, AbstractClassShapes
import math


class TestInheritance(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(4, 5)
        self.circle = Circle(7)

    def test_area_of_rectangle(self):
        self.assertEqual(self.rectangle.area(), 20, 'Area not calculated correctly')

    def test_perimeter_of_rectangle(self):
        self.assertEqual(self.rectangle.perimeter(), 18, 'Wrong calculation of perimeter')

    def test_rectangle_is_a_subclass_of_abstract_class_shape(self):
        self.assertIsInstance(self.rectangle, AbstractClassShapes, 'Rectangle not a subclass of Shape')

    def test_circle_is_an_instance_of_rectangle(self):
        self.assertIsInstance(self.circle, AbstractClassShapes, 'Circle is not an instance of class Shapes')

    def test_area_of_circle(self):
        self.assertEqual(self.circle.area(), math.pi * math.pow(7, 2), 'Area of circle not calculated correctly')

    def test_circumference_of_circle(self):
        self.assertEqual(self.circle.circumference(), math.pi * 2 * 7, 'Circumference of circle not calculated correctly')


if __name__ == '__main__':
    unittest.main()
