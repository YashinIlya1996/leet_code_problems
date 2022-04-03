""" https://leetcode.com/problems/next-permutation/ """
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if all([nums[i] >= nums[i + 1] for i in range(len(nums) - 1)]):
            nums.sort()
            return

        current = -2

        while True:
            less_than_cur = [x for x in nums[current + 1:] if x > nums[current]]
            if less_than_cur:
                to_swap = min(less_than_cur)
                to_replace = nums[current + 1:]
                to_replace.remove(to_swap)
                to_replace.append(nums[current])
                to_replace.sort()
                nums[current] = to_swap
                nums[current + 1:] = to_replace
                return
            current -= 1


if __name__ == '__main__':
    # l = [1, 2, 3, 3, 4, 4, 5, 5]
    l = [5, 5, 4, 3, 3, 2, 2, 1]
    Solution().nextPermutation(l)
