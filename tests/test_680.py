import unittest
import random
from string import ascii_lowercase
from valid_palindrome_ii_680 import Solution


class TestPalindromeInsert(unittest.TestCase):
    def test_first_lc_example(self):
        s = "aba"
        self.assertTrue(Solution().validPalindrome(s))

    def test_second_lc_example(self):
        s = "abca"
        self.assertTrue(Solution().validPalindrome(s))

    def test_third_lc_example(self):
        s = "abc"
        self.assertFalse(Solution().validPalindrome(s))

    def test_random_possible_insert(self):
        s = "".join(random.choices(ascii_lowercase, k=25))
        s += s[::-1]
        pos = random.randint(0, len(s) - 1)
        s = s[:pos] + random.choice(ascii_lowercase) + s[pos:]
        self.assertTrue(Solution().validPalindrome(s))

    def test_random_possible(self):
        s = "".join(random.choices(ascii_lowercase, k=25))
        s += s[::-1]
        self.assertTrue(Solution().validPalindrome(s))

    def test_regress(self):
        s = "ebcbbececabbacecbbcbe"
        self.assertTrue(Solution().validPalindrome(s))


if __name__ == '__main__':
    unittest.main()
