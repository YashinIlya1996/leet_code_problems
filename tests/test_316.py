import unittest
from remove_duplicate_letters_316 import Solution


class MyTestCase(unittest.TestCase):
    def test_simplest_test(self):
        self.assertEqual(Solution().removeDuplicateLetters("abca"), "abc")

    def test_simple(self):
        self.assertEqual(Solution().removeDuplicateLetters("bcabc"), "abc")

    def test_with_variants(self):
        self.assertEqual(Solution().removeDuplicateLetters("cbacdcbc"), "acdb")

    def test_my_example(self):
        self.assertEqual(Solution().removeDuplicateLetters("abadcdbcabdbdbcdaka"), "abcdk")

    def test_about_not_removing_previous(self):
        self.assertEqual(Solution().removeDuplicateLetters("abacb"), "abc")

    def test_xxx(self):
        self.assertEqual(Solution().removeDuplicateLetters("bbcaac"), "bac")

    def test_random_single(self):
        from random import choice
        from string import ascii_lowercase
        char = choice(ascii_lowercase)
        self.assertEqual(Solution().removeDuplicateLetters(char), char)


if __name__ == '__main__':
    unittest.main()
