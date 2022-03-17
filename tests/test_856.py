import unittest
from score_of_parentheses_856 import Solution

class TestScoreParentheses(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution().scoreOfParentheses

    def test_single_true_case(self):
        s = "()"
        self.assertEqual(self.solver(s), 1)

    def test_single_nesting(self):
        s = "(())"
        self.assertEqual(self.solver(s), 2)

    def test_double_nesting(self):
        s = "((()))"
        self.assertEqual(self.solver(s), 4)

    def test_complex_case(self):
        s = "(((()(()))))"
        self.assertEqual(self.solver(s), 24)

    def test_many_single_nested(self):
        s = "((()()()()()))"
        self.assertEqual(self.solver(s), 20)

    def test_s_podvohoy(self):
        s = "(())()"
        self.assertEqual(self.solver(s), 3)

if __name__ == '__main__':
    unittest.main()
