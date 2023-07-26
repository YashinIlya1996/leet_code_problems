""" https://leetcode.com/problems/minimum-speed-to-arrive-on-time/ """
from typing import List
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        def find_time(speed: int) -> float:
            return sum(ceil(dist[i] / speed) for i in range(len(dist) - 1)) + dist[-1] / speed

        hi, lo = 1e7, 1
        while lo < hi:
            cur = int(lo + (hi - lo) / 2)
            ft = find_time(cur)
            if ft > hour:
                lo = cur + 1
            elif ft < hour:
                hi = cur
            else:
                return cur

        return cur if find_time(cur) <= hour else cur + 1


if __name__ == '__main__':
    tests = (
        ([1, 3, 2], 6),
        ([1, 3, 2], 2.7),
        ([1, 3, 2], 2.4),
        ([2, 1, 5, 4, 4, 3, 2, 9, 2, 10], 75.12),
        ([1, 1], 1.0),
    )
    for dist, time in tests:
        print(Solution().minSpeedOnTime(dist, time))
