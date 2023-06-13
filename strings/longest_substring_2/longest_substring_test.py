import unittest

from longest_substring import length_of_longest_substring


class Test(unittest.TestCase):
    test_cases = [
        ("abccabb", 3),
        ("abcbdca", 4),
        ("", 0),
    ]

    test_functions = [
        length_of_longest_substring
    ]

    def test_find_two_sum(self):
        for longest_func in self.test_functions:
            for string, expected in self.test_cases:
                self.assertEqual(longest_func(string), expected)


if __name__ == '__main__':
    unittest.main()
