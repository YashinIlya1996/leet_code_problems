""" https://leetcode.com/problems/split-array-largest-sum/ """
from typing import List
from functools import cache

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """ Решение с помощью динамического программирования сверху вниз с кэшем """
        if m == 1:
            return sum(nums)
        length = len(nums)

        if m == length:
            return max(nums)

        sums = [0]  # sums[i] - сумма чисел в подмассиве с 0 до i, чтобы не вычислять каждый раз сумму заново
        for i in range(length):
            sums.append(sums[-1] + nums[i])

        @cache
        def min_max_sum(cur_pos, m):
            if m == 1:
                # случай, когда разбивать больше не можем из-за ограничения на количество подсписков
                return sums[length] - sums[cur_pos]

            min_of_all = float("inf")
            for i in range(cur_pos, length - m + 1):
                # проходим по каждому возможному подсписку и ищем максимальный
                first = sums[i + 1] - sums[cur_pos]
                another_max = max(first, min_max_sum(i + 1, m - 1))
                min_of_all = min(min_of_all, another_max)
                if first >= min_of_all:
                    # дальше итерировать нет смысла, т.к. первый подсписок будет только увеличиваться
                    break
            return min_of_all

        return min_max_sum(0, m)
