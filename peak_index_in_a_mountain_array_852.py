""" https://leetcode.com/problems/peak-index-in-a-mountain-array/ """


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr)
        if hi == 3:
            return 1
        while True:
            cur = (hi - lo) // 2 + lo
            pprev, p, pnext = arr[cur - 1], arr[cur], arr[cur + 1]
            if pprev < p > pnext:
                return cur
            elif pprev < p < pnext:
                lo = cur
            else:
                hi = cur


cases = (
    [0, 1, 0],
    [0, 2, 1, 0],
    [0, 10, 5, 2],
    [0, 1, 2, 3, 4, 5, 76, 98, 6, 5, 4, 3, 2, 1],
    [40, 48, 61, 75, 100, 99, 98, 39, 30, 10],
)
for case in cases:
    print(case, ':', Solution().peakIndexInMountainArray(case))
