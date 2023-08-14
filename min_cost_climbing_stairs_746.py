""" https://leetcode.com/problems/min-cost-climbing-stairs/ """

from functools import cache
from typing import List


class SolutionTopDown:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def get_min_cost(ind: int):
            if ind < 2:
                return cost[ind]
            else:
                return min(cost[ind] + get_min_cost(ind - 1), cost[ind] + get_min_cost(ind - 2))

        return min(get_min_cost(len(cost) - 1), get_min_cost(len(cost) - 2))


class SolutionBottomUp:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = cost[:2] + [0 for _ in range(len(cost) - 2)]
        for i in range(2, len(cost)):
            min_costs[i] = cost[i] + min(min_costs[i - 1], min_costs[i - 2])
        return min(min_costs[-2:])


if __name__ == '__main__':
    testcases = (
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 0, 1, 1], 1),
        ([0, 1, 1, 0], 1),
    )
    for solution_class in (SolutionBottomUp, SolutionTopDown):
        print(f'Testing {solution_class.__name__}')
        for data, expected in testcases:
            value = solution_class().minCostClimbingStairs(data)
            res = 'Success!' if value == expected else 'FAILED'
            print(f'{res:<10} data = {str(data):<50} {expected = :<10} {value = :<10}')
        print('-' * 120)
