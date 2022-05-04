import unittest
from max_number_of_k_sum_pairs_1679 import Solution


class KSummTest(unittest.TestCase):
    def test_first_lc_example(self):
        nums = [1, 2, 3, 4]
        k = 5
        self.assertEqual(Solution().maxOperations(nums, k), 2)

    def test_second_lc_example(self):
        nums = [3, 1, 3, 4, 3]
        k = 6
        self.assertEqual(Solution().maxOperations(nums, k), 1)


if __name__ == '__main__':
    unittest.main()
