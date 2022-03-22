import unittest
from random import randint, choice
from string import ascii_lowercase
from smallest_string_with_a_given_numeric_value_1663 import Solution


class TestNumericValueString(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(Solution().getSmallestString(3, 27), 'aay')

    def test_second_example(self):
        self.assertEqual(Solution().getSmallestString(5, 73), 'aaszz')

    def test_symbols_count(self):
        n = randint(1, 100_000)
        k = randint(n, 26 * n)
        result = Solution().getSmallestString(n, k)
        self.assertEqual(len(result), n)

    def test_single_char(self):
        k = randint(1, 26)
        char = ascii_lowercase[k - 1]
        self.assertEqual(Solution().getSmallestString(1, k), char)



if __name__ == '__main__':
    unittest.main()
