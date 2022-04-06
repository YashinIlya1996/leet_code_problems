import unittest
from IIIsum_with_multiplicity_923 import Solution


class TestIIISum(unittest.TestCase):
    def test_leetcode_example(self):
        l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        target = 8
        answer = 20
        self.assertEqual(Solution().threeSumMulti(l, target), answer)

    def test_simpler_leetcode_example(self):
        l = [1, 1, 2, 2, 2, 2]
        target = 5
        answer = 12
        self.assertEqual(Solution().threeSumMulti(l, target), answer)

    def test_three_zeros(self):
        l = [0, 0, 0]
        target = 0
        answer = 1
        self.assertEqual(Solution().threeSumMulti(l, target), answer)

    def test_three_numbers_impossible(self):
        l = [0, 7, 24]
        target = 15
        answer = 0
        self.assertEqual(Solution().threeSumMulti(l, target), answer)

    def test_three_numbers_possible(self):
        l = [0, 7, 24]
        target = 31
        answer = 1
        self.assertEqual(Solution().threeSumMulti(l, target), answer)

    def test_regress(self):
        l = [1, 2, 0, 3, 2, 0, 0, 2, 1]
        target = 2
        answer = 12
        self.assertEqual(Solution().threeSumMulti(l, target), answer)

    def test_regress2(self):
        l = [52, 53, 86, 11, 35, 1, 41, 34, 52, 64, 90, 54, 84, 99, 67, 8, 80, 100, 51, 66, 37, 31, 13, 13, 22, 31, 81,
             96, 81, 96]
        target = 79
        answer = 10
        self.assertEqual(Solution().threeSumMulti(l, target), answer)


if __name__ == '__main__':
    unittest.main()
