import unittest
from search_a_2d_matrix_74 import Solution


class MatrixSearchTest(unittest.TestCase):
    def test_target_in_first_elements(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [21, 22, 23, 24], [27, 30, 34, 60]]
        target = 1
        self.assertTrue(Solution().searchMatrix(matrix, target))

    def test_target_not_in_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(Solution().searchMatrix(matrix, target))

    def test_target_not_in_first_row(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [21, 22, 23, 24], [27, 30, 34, 60]]
        target = 60
        self.assertTrue(Solution().searchMatrix(matrix, target))


if __name__ == '__main__':
    unittest.main()
