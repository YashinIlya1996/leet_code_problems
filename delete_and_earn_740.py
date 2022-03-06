""" https://leetcode.com/problems/delete-and-earn/ """

from random import randint
from collections import Counter
from functools import cache
from sys import setrecursionlimit

MAX = 10 ** 4
setrecursionlimit(2 * MAX)
LENGTH = 20_000

a = [randint(1, MAX) for _ in range(LENGTH + 1)]
c = Counter(a)
b = [c[i] for i in range(0, max(a) + 1)]


@cache
def find_answer(n: int):
    if n == 1:
        return b[1]
    elif n == 2:
        return max(b[1], 2 * b[2])
    else:
        return max(n * b[n] + find_answer(n - 2), find_answer(n - 1))


print(find_answer(len(b) - 1))
