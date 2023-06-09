import unittest

from container_water import get_max_water_container, get_max_water_container_opt


class Test(unittest.TestCase):
    test_cases = [
        ([7, 1, 2, 3, 9], 28),
        ([1], 0),
        ([5, 6, 0], 5),
    ]

    test_functions = [
        get_max_water_container,
        get_max_water_container_opt
    ]

    def test_get_max_water_container(self):
        for water_fun in self.test_functions:
            for heights, expected in self.test_cases:
                self.assertEqual(water_fun(heights), expected)


if __name__ == '__main__':
    unittest.main()
