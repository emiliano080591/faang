import unittest

from arrays.rotation.left_rotation import rotLeft


class Test(unittest.TestCase):
    test_cases = [
        ("1 2 3 4 5", 4, [5, 1, 2, 3, 4]),
        ("8 9 4 3", 3, [3, 8, 9, 4]),
    ]

    test_functions = [
        rotLeft
    ]

    def test_rotate_left(self):
        for rotate_function in self.test_functions:
            for nums, rotations, expected_array in self.test_cases:
                int_array = list(map(int, list(map(int, nums.rstrip().split()))))
                self.assertListEqual(rotate_function(int_array, rotations), expected_array)
