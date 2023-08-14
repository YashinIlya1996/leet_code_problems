""" https://leetcode.com/problems/house-robber/ """

from functools import cache
from typing import List


class SolutionTopDown:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rob_ind(ind: int):
            if ind == 0:
                return nums[0]
            elif ind == 1:
                return max(nums[:2])
            else:
                return max(rob_ind(ind - 1), nums[ind] + rob_ind(ind - 2))

        return rob_ind(len(nums) - 1)


class SolutionBottomUp:
    def rob(self, nums: List[int]) -> int:
        memo = [nums[0], max(nums[:2])] + [0 for _ in range(len(nums) - 2)]
        for i in range(2, len(nums)):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return max(memo[-2:])


if __name__ == '__main__':
    testcases = (
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
    )
    for solution_class in (SolutionTopDown, SolutionBottomUp):
        print(f'Testing {solution_class.__name__}')
        for data, expected in testcases:
            value = solution_class().rob(data)
            res = 'Success!' if value == expected else 'FAILED'
            print(f'{res:<10} data = {str(data):<50} {expected = :<10} {value = :<10}')
        print('-' * 120)
