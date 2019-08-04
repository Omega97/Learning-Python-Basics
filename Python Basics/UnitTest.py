import unittest


def my_method(x):
    return x + 1


class TestMyMethod(unittest.TestCase):

    def test_value(self):
        # test the method
        self.assertAlmostEqual(my_method(1), 2)

    def test_types(self):
        # check if the proper error is triggered
        self.assertRaises(TypeError, my_method, "s")
