import unittest

from parentheses_needed import min_remove_to_make_valid


class Test(unittest.TestCase):
    test_cases = [
        ("a)bc(d)", "abc(d)"),
        ("(ab(c)d", "ab(c)d"),
    ]

    test_functions = [
        min_remove_to_make_valid
    ]

    def test_min_parentheses(self):
        for min_parentheses_function in self.test_functions:
            for string, expected in self.test_cases:
                self.assertEqual(min_parentheses_function(string), expected)
