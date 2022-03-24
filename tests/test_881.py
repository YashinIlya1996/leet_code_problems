import unittest
from boats_to_save_people_881 import Solution


class BoatsTest(unittest.TestCase):
    def test_first_leetcode_example(self):
        self.assertEqual(Solution().numRescueBoats([1, 2], 3), 1)

    def test_second_leetcode_example(self):
        self.assertEqual(Solution().numRescueBoats([3, 2, 2, 1], 3), 3)

    def test_third_leetcode_example(self):
        self.assertEqual(Solution().numRescueBoats([3, 5, 3, 4], 5), 4)


if __name__ == '__main__':
    unittest.main()
