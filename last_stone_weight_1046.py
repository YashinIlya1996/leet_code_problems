""" https://leetcode.com/problems/last-stone-weight/ """
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq as h
        stones = [-s for s in stones]
        h.heapify(stones)
        while len(stones) > 1:
            a, b = h.heappop(stones), h.heappop(stones)
            if a != b:
                h.heappush(stones, -abs(a - b))
        return 0 if not stones else -stones[0]
