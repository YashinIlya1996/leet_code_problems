import unittest
from split_array_largest_sum_410 import Solution


class TestSplitArray(unittest.TestCase):
    def test_first_lc_example(self):
        self.assertEqual(Solution().splitArray([7, 2, 5, 10, 8], 2), 18)

    def test_second_lc_example(self):
        self.assertEqual(Solution().splitArray([1, 2, 3, 4, 5], 2), 9)

    def test_third_lc_example(self):
        self.assertEqual(Solution().splitArray([1, 4, 4], 3), 4)


if __name__ == '__main__':
    unittest.main()
