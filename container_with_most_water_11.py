""" https://leetcode.com/problems/container-with-most-water/ """
from typing import List


class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     """ Первое решение не проходит по времени"""
    #     max_areas = []
    #     n = len(height)
    #     current_max_h = 0
    #     for num, h in enumerate(height):
    #         current_max_area = 0
    #         if h > current_max_h:
    #             for i in range(n - 1, num - 1, -1):
    #                 area = (i - num) * min(h, height[i])
    #                 if area > current_max_area:
    #                     current_max_area = area
    #                     if h <= height[i]:
    #                         break
    #             max_areas.append(current_max_area)
    #             current_max_h = h
    #     return max(max_areas)

    def maxArea(self, height: List[int]) -> int:
        """ Жадный алгоритм - оставляем максимальным расстояние между стенками,
            ищем наибольшую высоту, прошел по времени. """
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0

        def area():
            return (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])

        while left_pointer < right_pointer:
            cur_area = area()
            max_area = max(max_area, cur_area)
            if height[left_pointer] > height[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1

        return max_area
