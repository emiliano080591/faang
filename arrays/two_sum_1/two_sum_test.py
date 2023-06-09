import unittest
from two_sum import find_two_sum,find_two_sum_opt


class Test(unittest.TestCase):
    test_cases = [
        ([5, 48, 32], 37, [0, 2]),
        ([5, 48, 32], 53, [0, 1]),
        ([5, 48, 32], 5, None),
    ]

    test_functions = [
        find_two_sum,
        find_two_sum_opt
    ]

    def test_find_two_sum(self):
        for sum_fun in self.test_functions:
            for nums, target, expected in self.test_cases:
                self.assertEqual(sum_fun(nums, target), expected)


if __name__ == '__main__':
    unittest.main()
