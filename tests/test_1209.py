import unittest
import re
from remove_all_adjacent_duplicates_in_string_ii_1209 import Solution

class TestRemoveDuplicatesII(unittest.TestCase):
    @staticmethod
    def answer(s: str, k: int) -> str:
        pattern = r'((.)\2{' + str(k - 1) + '})'
        pattern = re.compile(pattern)
        match = re.findall(pattern, s)
        while match:
            duplicates = [c[0] for c in match]
            for duplicate in duplicates:
                s = s.replace(duplicate, '')
            match = re.findall(pattern, s)
        return s


    def test_first_lc_example(self):
        s = 'abcd'
        k = 2
        expected = TestRemoveDuplicatesII.answer(s, k)
        self.assertEqual(Solution().removeDuplicates(s, k), expected)

    def test_second_lc_example(self):
        s = 'deeedbbcccbdaa'
        k = 3
        expected = TestRemoveDuplicatesII.answer(s, k)
        self.assertEqual(Solution().removeDuplicates(s, k), expected)

    def test_third_lc_example(self):
        s = 'pbbcggttciiippooaais'
        k = 2
        expected = TestRemoveDuplicatesII.answer(s, k)
        self.assertEqual(Solution().removeDuplicates(s, k), expected)

    def test_big_example(self):
        with open('../temp/1209_in.txt', 'rt') as f:
            s = f.readline()
        k = 2
        expected = ''
        self.assertEqual(Solution().removeDuplicates(s, k), expected)


if __name__ == '__main__':
    unittest.main()
