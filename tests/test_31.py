import unittest
from next_permutation_31 import Solution


class NextPermutationTest(unittest.TestCase):
    def test_last_permutation(self):
        l = [5, 5, 4, 3, 3, 2, 2, 2, 1, 1]
        old_l = l.copy()
        Solution().nextPermutation(l)
        self.assertEqual(l, sorted(old_l))

    def test_simple_132(self):
        l = [1, 3, 2]
        next_perm = [2, 1, 3]
        Solution().nextPermutation(l)
        self.assertEqual(l, next_perm)

    def test_harder_without_repeat_only_digits(self):
        l = [5, 7, 6, 3, 4, 1, 2, 8, 9]
        next_perm = [5, 7, 6, 3, 4, 1, 2, 9, 8]
        Solution().nextPermutation(l)
        self.assertEqual(l, next_perm)

    def test_harder_with_repeat_only_digits(self):
        l = [3, 4, 5, 4, 6, 7, 5, 2, 3, 1, 1]
        next_perm = [3, 4, 5, 4, 6, 7, 5, 3, 1, 1, 2]
        Solution().nextPermutation(l)
        self.assertEqual(l, next_perm)

    def test_with_repeat_with_numbers(self):
        l = [31, 34, 1, 1, 2, 90, 76, 43, 34, 31]
        next_perm = [31, 34, 1, 1, 31, 2, 34, 43, 76, 90]
        Solution().nextPermutation(l)
        self.assertEqual(l, next_perm)

if __name__ == '__main__':
    unittest.main()
