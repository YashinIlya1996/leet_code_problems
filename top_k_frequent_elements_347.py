""" https://leetcode.com/problems/top-k-frequent-elements/ """
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(c := Counter(nums), key=lambda x: c[x])[-k:]
