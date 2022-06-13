""" https://leetcode.com/problems/maximum-erasure-value/ """
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        from collections import deque
        d = deque()
        sums, s = set(), set()
        current_sum = 0
        for num in nums:
            if num in s:
                while num in s:
                    el = d.popleft()
                    current_sum -= el
                    s.remove(el)
            current_sum += num
            s.add(num)
            d.append(num)
            sums.add(current_sum)

        return max(sums)


