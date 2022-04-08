""" https://leetcode.com/problems/kth-largest-element-in-a-stream/ """
import bisect
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.knums = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.knums) < self.k:
            bisect.insort(self.knums, val)
            return self.knums[0]
        if val <= self.knums[0]:
            return self.knums[0]
        del self.knums[0]
        bisect.insort(self.knums, val)
        return self.knums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)