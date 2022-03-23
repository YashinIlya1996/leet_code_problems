""" https://leetcode.com/problems/permutation-sequence/ """


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """ Медленное жульничество, пойдет для тестов в будущем """
        from itertools import permutations
        p = permutations([i for i in range(1, n + 1)])
        for _ in range(k - 1):
            next(p)
        return "".join(map(str, (next(p))))
