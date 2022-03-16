import unittest
from validate_stack_sequences_946 import Solution


class TestSolution(unittest.TestCase):

    def test_true_case(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 5, 3, 2, 1]
        self.assertTrue(Solution().validateStackSequences(pushed, popped))

    def test_reversed_true_case(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [5, 4, 3, 2, 1]
        self.assertTrue(Solution().validateStackSequences(pushed, popped))

    def test_false_case(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 3, 5, 1, 2]
        self.assertFalse(Solution().validateStackSequences(pushed, popped))

    def test_one_element_stack(self):
        from random import randint
        pushed = [randint(0, 1000)]
        popped = pushed.copy()
        self.assertTrue(Solution().validateStackSequences(pushed, popped))


if __name__ == '__main__':
    unittest.main()
