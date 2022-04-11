""" https://leetcode.com/problems/shift-2d-grid/ """
from typing import List
from itertools import chain


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k = k % m
        nums = list(chain.from_iterable(grid))
        nums = nums[-k:] + nums[:-k]
        return [nums[i * n:(i + 1) * n] for i in range(m)]
