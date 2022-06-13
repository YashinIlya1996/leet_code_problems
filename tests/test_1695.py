import unittest
from maximum_erasure_value_1695 import Solution


class TestMaxErasureValue(unittest.TestCase):
    def test_first_lc_example(self):
        in_data = [4, 2, 4, 5, 6]
        output = 17
        self.assertEqual(Solution().maximumUniqueSubarray(in_data), output)

    def test_second_lc_example(self):
        in_data = [5, 2, 1, 2, 5, 2, 1, 2, 5]
        output = 8
        self.assertEqual(Solution().maximumUniqueSubarray(in_data), output)


if __name__ == '__main__':
    unittest.main()