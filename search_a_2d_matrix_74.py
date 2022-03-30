""" https://leetcode.com/problems/search-a-2d-matrix/ """
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_elements = [row[0] for row in matrix]
        left = 0
        right = len(first_elements) - 1
        while left <= right:
            mid = (left + right) // 2
            if first_elements[mid] == target:
                return True
            elif mid != len(first_elements) - 1 and first_elements[mid] < target < first_elements[mid + 1]:
                break
            elif first_elements[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        potential_row = matrix[mid]
        left = 0
        right = len(potential_row) - 1
        while left <= right:
            mid = (left + right) // 2
            if potential_row[mid] == target:
                return True
            elif potential_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
