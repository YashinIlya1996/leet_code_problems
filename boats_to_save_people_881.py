""" https://leetcode.com/problems/boats-to-save-people/ """
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
          Применяем жадный алгоритм на отсортированном массиве. Если самый тяжелый человек может взять самого легкого -
        он это делает (см. смещение указателей), иначе - садится в лодку один.
        """
        people.sort()
        light_pointer = 0
        heavy_pointer = len(people) - 1
        boats = 0
        while light_pointer <= heavy_pointer:
            if people[light_pointer] + people[heavy_pointer] <= limit:
                light_pointer += 1
                heavy_pointer -= 1
            else:
                heavy_pointer -= 1
            boats += 1
        return boats
