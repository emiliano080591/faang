import unittest

from stacks.valid_parentheses_1.valid_parentheses import is_valid_parentheses


class Test(unittest.TestCase):
    test_cases = [
        ("[{()}]", True),
        ("((()])", False),
    ]

    test_functions = [
        is_valid_parentheses
    ]

    def test_valid_parentheses(self):
        for valid_parentheses_function in self.test_functions:
            for string, expected in self.test_cases:
                self.assertEqual(valid_parentheses_function(string), expected)
