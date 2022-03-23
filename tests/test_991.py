import unittest
from random import randint

from broken_calculator_991 import Solution


class TestBrokenCalculator(unittest.TestCase):
    def test_first_leetcode_example(self):
        self.assertEqual(Solution().brokenCalc(2, 3), 2)

    def test_second_leetcode_example(self):
        self.assertEqual(Solution().brokenCalc(5, 8), 2)

    def test_third_leetcode_example(self):
        self.assertEqual(Solution().brokenCalc(3, 10), 3)

    def test_equal_values(self):
        val = randint(1, 10 ** 9)
        self.assertEqual(Solution().brokenCalc(val, val), 0)

    def test_target_lt_start(self):
        start = randint(1, 10 ** 9)
        target = randint(1, start)
        self.assertEqual(Solution().brokenCalc(start, target), start - target)


if __name__ == '__main__':
    unittest.main()
