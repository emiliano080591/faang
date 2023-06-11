import unittest
from rain_water import get_trapped_rain_water,get_trapped_rain_water_opt


class Test(unittest.TestCase):
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ]

    test_functions = [
        get_trapped_rain_water,
        get_trapped_rain_water_opt
    ]

    def test_get_max_water_container(self):
        for rain_function in self.test_functions:
            for heights, expected in self.test_cases:
                self.assertEqual(rain_function(heights), expected)


if __name__ == '__main__':
    unittest.main()
