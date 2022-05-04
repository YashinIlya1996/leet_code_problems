import unittest
from spiral_matrix_ii_59 import Solution


class SpiralTest(unittest.TestCase):
    def test_odd(self):
        n = 5
        spiral = [[1, 2, 3, 4, 5],
                  [16, 17, 18, 19, 6],
                  [15, 24, 25, 20, 7],
                  [14, 23, 22, 21, 8],
                  [13, 12, 11, 10, 9]]
        self.assertEqual(Solution().generateMatrix(n), spiral)

    def test_even(self):
        n = 4
        spiral = [[1, 2, 3, 4],
                  [12, 13, 14, 5],
                  [11, 16, 15, 6],
                  [10, 9, 8, 7]]
        self.assertEqual(Solution().generateMatrix(n), spiral)

    def test_n_equal_one(self):
        n = 1
        spiral = [[1]]
        self.assertEqual(Solution().generateMatrix(n), spiral)

if __name__ == '__main__':
    unittest.main()
