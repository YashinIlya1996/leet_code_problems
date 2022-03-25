""" https://leetcode.com/problems/two-city-scheduling/ """
from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Использует жадный алгоритм - сначала сортируем по разнице стоимости рейсов в города
        Из первой половины листа берем билеты для города a, из второго - для b
        """
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        for i in range(len(costs) // 2):
            total += costs[i][0] + costs[-i - 1][1]
        return total
