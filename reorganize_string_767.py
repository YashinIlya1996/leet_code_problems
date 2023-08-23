""" https://leetcode.com/problems/reorganize-string/ """
import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s

        counter = collections.Counter(s)
        limit = len(s) // 2 + (len(s) % 2)
        if any(v > limit for v in counter.values()):
            return ""

        def chargen():
            mc = counter.most_common()
            for char, count in mc:
                yield from char * count

        g = chargen()
        res = [None] * len(s)
        for ind in range(0, len(s), 2):
            res[ind] = next(g)
        for ind in range(1, len(s), 2):
            res[ind] = next(g)
        return ''.join(res)
