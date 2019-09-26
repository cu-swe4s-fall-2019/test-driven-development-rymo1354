import unittest
import get_data
import sys


class TestColumnNull(unittest.TestCase):
    def test_read_stdin_col_null(self):
        self.assertRaises(TypeError, get_data.read_stdin_col, None)


if __name__ == '__main__':
    unittest.main()
