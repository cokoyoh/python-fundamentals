import unittest
import recurive_functions as recurive


class TestRecursiveFactorials(unittest.TestCase):

    def test_can_return_the_factorial_of_zero_as_one(self):
        self.assertEqual(recurive.factorial(0), 1)


if __name__ == '__main__':
    unittest.main()