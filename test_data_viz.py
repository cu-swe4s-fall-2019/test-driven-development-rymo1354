import unittest
import os
import data_viz
import stat


class TestBoxPlot(unittest.TestCase):
    def test_boxplot_null(self):
        self.assertRaises(TypeError, data_viz.boxplot, None)

    def test_boxplot_empty_list(self):
        self.assertRaises(IndexError, data_viz.boxplot, [])

    def test_boxplot_wrong_type(self):
        self.assertRaises(TypeError, data_viz.boxplot, 'test')
        self.assertRaises(TypeError, data_viz.boxplot, 3)
        self.assertRaises(TypeError, data_viz.boxplot, False)

    def test_boxplot_list_wrong_type(self):
        self.assertRaises(TypeError, data_viz.boxplot,
                          ['bad', 1, ['bad']])

    def test_boxplot_filename_str(self):
        self.assertRaises(TypeError, data_viz.boxplot, [1, 2, 3],
                          1)

    def test_boxplot_write_to_file(self):
        data_viz.boxplot([1, 2, 3], 'newfile.png')
        self.assertTrue(os.path.exists("newfile.png"))
        os.remove("newfile.png")

    def test_boxplot_permission(self):
        with open("read_only.png", "w") as f:
            f.write("No Access")
        os.chmod("read_only.png", stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        self.assertRaises(PermissionError, data_viz.boxplot, [
                          1, 2, 3, 4, 5], "read_only.png")
        os.remove("read_only.png")

    def test_boxplot_wrong_file(self):
        self.assertRaises(ValueError, data_viz.boxplot,
                          [1, 2, 3, 4, 5], "read_only.txt")


class TestHistogram(unittest.TestCase):
    def test_histogram_null(self):
        self.assertRaises(TypeError, data_viz.histogram, None)

    def test_histogram_empty_list(self):
        self.assertRaises(IndexError, data_viz.histogram, [])

    def test_histogram_wrong_type(self):
        self.assertRaises(TypeError, data_viz.histogram, 'test')
        self.assertRaises(TypeError, data_viz.histogram, 3)
        self.assertRaises(TypeError, data_viz.histogram, False)

    def test_histogram_list_wrong_type(self):
        self.assertRaises(TypeError, data_viz.histogram,
                          ['bad', 1, ['bad']])

    def test_histogram_filename_str(self):
        self.assertRaises(TypeError, data_viz.histogram, [1, 2, 3],
                          1)

    def test_histogram_write_to_file(self):
        data_viz.histogram([1, 2, 3], 'newfile.png')
        self.assertTrue(os.path.exists("newfile.png"))
        os.remove("newfile.png")

    def test_histogram_permission(self):
        with open("read_only.png", "w") as f:
            f.write("No Access")
        os.chmod("read_only.png", stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        self.assertRaises(PermissionError, data_viz.histogram, [
                          1, 2, 3, 4, 5], "read_only.png")
        os.remove("read_only.png")

    def test_histogram_wrong_file(self):
        self.assertRaises(ValueError, data_viz.histogram,
                          [1, 2, 3, 4, 5], "read_only.txt")


class TestCombo(unittest.TestCase):
    def test_combo_null(self):
        self.assertRaises(TypeError, data_viz.combo, None)

    def test_combo_empty_list(self):
        self.assertRaises(IndexError, data_viz.combo, [])

    def test_combo_wrong_type(self):
        self.assertRaises(TypeError, data_viz.combo, 'test')
        self.assertRaises(TypeError, data_viz.combo, 3)
        self.assertRaises(TypeError, data_viz.combo, False)

    def test_combo_list_wrong_type(self):
        self.assertRaises(TypeError, data_viz.combo,
                          ['bad', 1, ['bad']])

    def test_combo_filename_str(self):
        self.assertRaises(TypeError, data_viz.combo, [1, 2, 3],
                          1)

    def test_combo_write_to_file(self):
        data_viz.combo([1, 2, 3], 'newfile.png')
        self.assertTrue(os.path.exists("newfile.png"))
        os.remove("newfile.png")

    def test_combo_permission(self):
        with open("read_only.png", "w") as f:
            f.write("No Access")
        os.chmod("read_only.png", stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        self.assertRaises(PermissionError, data_viz.combo, [
                          1, 2, 3, 4, 5], "read_only.png")
        os.remove("read_only.png")

    def test_combo_wrong_file(self):
        self.assertRaises(ValueError, data_viz.combo,
                          [1, 2, 3, 4, 5], "read_only.txt")


if __name__ == '__main__':
    unittest.main()
