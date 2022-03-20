""" https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ """
from typing import List
from collections import defaultdict, Counter


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Быстрая проверка на то, есть ли доминошки с парными значениями.
        Если их больше, чем одна, то поворотом доминошки значения не выровнять ни в каком случае.
        """
        duplicates = {key for key in zip(tops, bottoms) if key[0] == key[1]}
        if len(duplicates) > 1:
            return -1

        """
        Если есть парные доминошки только с одним значением, то проверить можно только на повороты с такими же значением
        """
        if duplicates:
            val = duplicates.pop()[0]
            rotates_t2b, rotates_b2t = 0, 0
            for domino in zip(tops, bottoms):
                if domino[0] != val and domino[1] != val:
                    return -1
                elif domino[0] == domino[1] == val:
                    pass
                else:
                    if domino[0] == val:
                        rotates_t2b += 1
                    else:
                        rotates_b2t += 1
            return min(rotates_t2b, rotates_b2t)


        """
        Последний вариант, когда все доминошки разные
        """
        length = len(tops)
        counter_top = Counter(tops)
        counter_bottom = Counter(bottoms)
        res = []
        if all([counter_top[i] + counter_bottom[i] < length for i in range(1, 7)]):
            return -1
        for i in range(1, 7):
            if counter_top[i] + counter_bottom[i] == length:
                res.append(min(length - counter_top[i], length - counter_bottom[i]))
        return min(res)
