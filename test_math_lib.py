import unittest
import math_lib


class TestNone(unittest.TestCase):

    def test_mean_none(self):
        self.assertEqual(math_lib.list_mean(None), None)

    def test_stdev_null(self):
        self.assertEqual(math_lib.list_stdev(None), None)


class TestString(unittest.TestCase):

    def test_mean_string(self):
        with self.assertRaises(TypeError):
            math_lib.list_mean('test')

    def test_stdev_string(self):
        with self.assertRaises(TypeError):
            math_lib.list_stdev('test')


class TestInteger(unittest.TestCase):

    def test_mean_integer(self):
        with self.assertRaises(TypeError):
            math_lib.list_mean(3)

    def test_stdev_integer(self):
        with self.assertRaises(TypeError):
            math_lib.list_stdev(3)


if __name__ == '__main__':
    unittest.main()
