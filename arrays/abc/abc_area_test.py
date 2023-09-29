import unittest

from arrays.abc.abc_area import designer_pdf_viewer


class Test(unittest.TestCase):
    test_cases = [
        ("1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5", "abc", 9),
        ("1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7", "zaba", 28),
    ]

    test_functions = [
        designer_pdf_viewer
    ]

    def test_designer_pdf_viewer(self):
        for pdf_viewer_function in self.test_functions:
            for heights, word, expected in self.test_cases:
                heights_array = list(map(int, list(map(int, heights.rstrip().split()))))
                self.assertEqual(pdf_viewer_function(heights_array, word), expected)
