""" https://leetcode.com/problems/arithmetic-slices/ """
from functools import cache


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:

        @cache
        def get_count_subarrays(num: int) -> int:
            return (num - 1) * (num - 2) // 2 if num >= 3 else 0

        answer = 0
        length_count = 0
        if len(nums) >= 3:
            difference = nums[1] - nums[0]
            length_count = 2
            for ind, el in enumerate(nums[1:-1], 1):
                if nums[ind + 1] - el == difference:
                    length_count += 1
                else:
                    answer += get_count_subarrays(length_count)
                    difference = nums[ind + 1] - el
                    length_count = 2

        return answer + get_count_subarrays(length_count)


s = Solution()
print(s.numberOfArithmeticSlices(list(map(int, input().split()))))
