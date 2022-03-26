""" https://leetcode.com/problems/binary-search/ """
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        current = (left + right) // 2
        while left <= right:
            if nums[current] == target:
                return current
            if nums[current] > target:
                right = current - 1
            else:
                left = current + 1
            current = (left + right) // 2
        return -1



