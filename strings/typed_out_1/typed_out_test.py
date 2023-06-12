import unittest

from typed_out import back_space_compare, back_space_compare_opt


class Test(unittest.TestCase):
    test_cases = [
        ("ab#z", "az#z", True),
        ("abc#d", "acc#c", False),
        ("x#y#z#", "a#", True),
        ("a###b", "b", True),
        ("Ab#z", "ab#z", False),
    ]

    test_functions = [
        back_space_compare,
        back_space_compare_opt
    ]

    def test_find_two_sum(self):
        for typed_func in self.test_functions:
            for s1, s2, expected in self.test_cases:
                self.assertEqual(typed_func(s1, s2), expected)


if __name__ == '__main__':
    unittest.main()
