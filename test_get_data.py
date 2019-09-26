import unittest
import get_data
import sys


class TestColumnNull(unittest.TestCase):
    def test_read_stdin_col_null(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, None)


class TestIncorrectValues(unittest.TestCase):
    def test_read_stdin_col_list_values(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, ['A', 'B', 'C'])

    def test_read_stdin_col_str_values(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, "A")

    def test_read_stdin_col_float_values(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, 5.4)


if __name__ == '__main__':
    unittest.main()
