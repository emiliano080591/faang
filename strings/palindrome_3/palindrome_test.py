import unittest

from palindrome import is_valid_palindrome


class Test(unittest.TestCase):
    test_cases = [
        ("abccdba", False),
        ("abcba", True),
        ("anitalavalatina", True),
    ]

    test_functions = [
        is_valid_palindrome
    ]

    def test_find_two_sum(self):
        for palindrome_func in self.test_functions:
            for string, expected in self.test_cases:
                self.assertEqual(palindrome_func(string), expected)


if __name__ == '__main__':
    unittest.main()
