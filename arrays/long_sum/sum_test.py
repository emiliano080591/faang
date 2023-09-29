import unittest

from arrays.long_sum.sum import a_very_big_sum


class Test(unittest.TestCase):
    test_cases = [
        ("10000005 10000004 10000003 10000002", 40000014),
        ("20000003 10000001 10000005 10000006", 50000015),
        ("10000001 10000002 10000003", 30000006),
    ]

    test_functions = [
        a_very_big_sum
    ]

    def test_a_ver_long_sum(self):
        for sum_function in self.test_functions:
            for nums, expected_sum in self.test_cases:
                int_array = list(map(int, list(map(int, nums.rstrip().split()))))
                self.assertEqual(sum_function(int_array), expected_sum)
