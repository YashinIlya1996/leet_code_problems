""" https://leetcode.com/problems/longest-consecutive-sequence/ """
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_, min_ = max(nums), min(nums)
        counter = [False] * (max_ - min_ + 1)
        for n in nums:
            counter[n - min_] = True
        cur, max_s = 0, 0
        for i in range(len(counter)):
            if counter[i]:
                cur += 1
                max_s = max(max_s, cur)
            else:
                cur = 0
        return max_s


if __name__ == '__main__':
    tests = (
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    )
    for nums, answer in tests:
        print(f'Data: {nums}; Expected: {answer}; Result: {Solution().longestConsecutive(nums)}')
