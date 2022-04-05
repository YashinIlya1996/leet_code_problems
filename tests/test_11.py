import unittest
from typing import List
from container_with_most_water_11 import Solution


class TestContainerWater(unittest.TestCase):
    @staticmethod
    def right_answer(height: List[int]) -> int:
        max_areas = []
        n = len(height)
        for num, h in enumerate(height):
            current_max_area = 0
            for i in range(n - 1, -1, -1):
                area = (i - num) * min(h, height[i])
                if area > current_max_area:
                    current_max_area = area
                    if h <= height[i]:
                        break
            max_areas.append(current_max_area)
        return max(max_areas)

    def test_11_equal_1(self):
        self.assertEqual(Solution().maxArea([1, 1]), 1)

    def test_leetcode_example(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        answer = 49
        self.assertEqual(Solution().maxArea(height), answer)

    def test_leetcode_fail_example(self):
        height = [2, 3, 4, 5, 18, 17, 6]
        answer = TestContainerWater.right_answer(height)
        self.assertEqual(Solution().maxArea(height), answer)

    def test_random_values(self):
        from random import randint
        n = 1000
        MAX = 1000
        height = [randint(0, MAX) for _ in range(n)]
        answer = TestContainerWater.right_answer(height)
        self.assertEqual(Solution().maxArea(height), answer)


if __name__ == '__main__':
    unittest.main()
