import unittest
from baseball_game_682 import Solution


class TestBaseball(unittest.TestCase):
    def test_first_lc_example(self):
        commands = ["5", "2", "C", "D", "+"]
        answer = 30
        self.assertEqual(Solution().calPoints(commands), answer)

    def test_second_lc_example(self):
        commands = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        answer = 27
        self.assertEqual(Solution().calPoints(commands), answer)

    def test_third_lc_example(self):
        commands = ["1"]
        answer = 1
        self.assertEqual(Solution().calPoints(commands), answer)


if __name__ == '__main__':
    unittest.main()