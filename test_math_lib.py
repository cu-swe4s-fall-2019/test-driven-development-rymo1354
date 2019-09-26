import unittest
import math_lib
import random
import statistics


class TestNone(unittest.TestCase):

    def test_mean_none(self):
        with self.assertRaises(TypeError):
            math_lib.list_mean(None)

    def test_stdev_none(self):
        with self.assertRaises(TypeError):
            math_lib.list_stdev(None)


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


class TestFloat(unittest.TestCase):

    def test_mean_float(self):
        with self.assertRaises(TypeError):
            math_lib.list_mean(3.5)

    def test_stdev_float(self):
        with self.assertRaises(TypeError):
            math_lib.list_stdev(3.5)


class TestBoolean(unittest.TestCase):

    def test_mean_boolean(self):
        with self.assertRaises(TypeError):
            math_lib.list_mean(False)

    def test_stdev_boolean(self):
        with self.assertRaises(TypeError):
            math_lib.list_stdev(True)


class TestEmptyArray(unittest.TestCase):

    def test_mean_empty(self):
        with self.assertRaises(ZeroDivisionError):
            math_lib.list_mean([])

    def test_stdev_empty(self):
        with self.assertRaises(ZeroDivisionError):
            math_lib.list_stdev([])


class TestRandomArray(unittest.TestCase):

    def test_mean_random(self):

        A = []

        for i in range(50):
            A.append(random.uniform(1, 100))
            A.append(random.randint(1, 100))

        self.assertAlmostEqual(math_lib.list_mean(A),
                               statistics.mean(A))

    def test_stdev_random(self):

        A = []

        for i in range(50):
            A.append(random.uniform(1, 100))
            A.append(random.randint(1, 100))

        self.assertAlmostEqual(math_lib.list_stdev(A),
                               statistics.pstdev(A))


class TestBadArray(unittest.TestCase):

    def test_mean_bad(self):
        with self.assertRaises(TypeError):
            math_lib.list_mean(['B', 'A', 3])

    def test_stdev_bad(self):
        with self.assertRaises(TypeError):
            math_lib.list_stdev([1, [], 3])


if __name__ == '__main__':
    unittest.main()
