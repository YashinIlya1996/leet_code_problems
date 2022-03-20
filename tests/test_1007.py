import unittest
from minimum_domino_rotations_for_equal_row_1007 import Solution


class DominoRotationTest(unittest.TestCase):
    def tearDown(self) -> None:
        self.assertEqual(Solution().minDominoRotations(self.t, self.b), self.answer)
        self.assertEqual(Solution().minDominoRotations(self.b, self.t), self.answer)

    def test_some_dominos(self):
        self.t = [1, 2, 3, 4, 5]
        self.b = [2, 2, 4, 5, 5]
        self.answer = -1

    def test_first_leetcode_example(self):
        self.t = [2, 1, 2, 4, 2, 2]
        self.b = [5, 2, 6, 2, 3, 2]
        self.answer = 2

    def test_all_different_cannot(self):
        self.t = [3, 5, 1, 2, 3]
        self.b = [6, 6, 3, 3, 4]
        self.answer = -1

    def test_second_leetcode_example(self):
        self.t = [3, 5, 1, 2, 3]
        self.b = [3, 6, 3, 3, 4]
        self.answer = -1

    def test_all_different_can(self):
        self.t = [2, 1, 2, 4, 2, 2]
        self.b = [5, 2, 6, 2, 3, 1]
        self.answer = 2



if __name__ == '__main__':
    unittest.main()
