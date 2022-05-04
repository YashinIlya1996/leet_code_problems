""" https://leetcode.com/problems/max-number-of-k-sum-pairs/ """
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        hm = defaultdict(int)
        answer = 0
        for el in nums:
            if el <= k:
                opposite = hm[k - el]
                if opposite:
                    answer += 1
                    hm[k - el] -= 1
                else:
                    hm[el] += 1
        return answer
