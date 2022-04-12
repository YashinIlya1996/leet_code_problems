import unittest
from game_of_life_289 import Solution


class LifeTest(unittest.TestCase):
    def test_1_lc_example(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        answer = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        Solution().gameOfLife(board)
        self.assertEqual(board, answer)

    def test_2_lc_example(self):
        board = [[1, 1], [1, 0]]
        answer = [[1, 1], [1, 1]]
        Solution().gameOfLife(board)
        self.assertEqual(board, answer)


if __name__ == '__main__':
    unittest.main()