import unittest
import random
from counting_bits_338 import Solution


class BitsTest(unittest.TestCase):
    @staticmethod
    def answer(n):
        return [bin(x).count('1') for x in range(n + 1)]

    def test_anything(self):
        n = random.randint(0, 1000)
        self.assertEqual(Solution().countBits(n), self.answer(n))


if __name__ == '__main__':
    pass
