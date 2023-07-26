""" https://leetcode.com/problems/maximum-sum-circular-subarray/ """


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if all(n >= 0 for n in nums):
            return sum(nums)
        p_tail, p_head = 0, 0
        extended_nums = nums * 2
        max_index = len(extended_nums) - 1
        s_max, s_cur = nums[0], 0
        while p_head < max_index or p_tail < max_index:
            if p_head < max_index and p_head - p_tail < len(nums) - 1:
                s_cur += extended_nums[p_head]
                p_head += 1
            else:
                s_cur -= extended_nums[p_tail]
                p_tail += 1
            if s_cur > s_max:
                s_max = s_cur
            # if s_cur < 0:
            #     p_tail = p_head
            #     s_cur = 0
        return s_max


def check_answer(nums):
    answer = Solution().maxSubarraySumCircular(nums)
    print(f'{nums = }, {answer = }')


cases = (
    [5, 5, 0, -5, 3, -3, 2],
    [3, 1, 3, 2, 6],
    [3, 1, 3, -2, 6],
    [-2],
    [3],
    [1, -2, 3, -2],
    [5, -3, 5],
    [-3, -2, -3],
    [6, 9, -3, -1, 3, -8],
)

for case in cases:
    check_answer(case)
