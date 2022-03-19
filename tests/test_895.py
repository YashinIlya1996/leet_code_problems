import unittest
from maximum_frequency_stack_895 import FreqStack


class FreqStackTest(unittest.TestCase):

    def test_push_check(self):
        fs = FreqStack()
        fs.push(5)
        self.assertEqual(fs.stack, [5])
        fs.push(7)
        self.assertEqual(fs.stack, [5, 7])
        fs.push(5)
        self.assertEqual(fs.stack, [5, 7, 5])
        fs.push(7)
        self.assertEqual(fs.stack, [5, 7, 5, 7])
        fs.push(4)
        self.assertEqual(fs.stack, [5, 7, 4, 5, 7])
        fs.push(5)
        self.assertEqual(fs.stack, [5, 7, 4, 5, 7, 5])


if __name__ == '__main__':
    unittest.main()
