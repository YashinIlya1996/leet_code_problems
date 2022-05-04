""" https://leetcode.com/problems/spiral-matrix-ii/ """
from typing import List
from itertools import cycle


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = ((1, 0), (0, -1), (-1, 0), (0, 1))  # down, left, up, right
        spiral = [[0] * n for _ in range(n)]
        spiral[0] = [i for i in range(1, n + 1)]  # first row
        iter_directions = cycle(directions)  # endless directions iter
        i, j, val = 0, n - 1, n     # first row already filled
        for length in range(n - 1, 0, -1):
            for _ in range(2):  # there are two sublists of same length (but different direction)
                dir = next(iter_directions)  # change direction
                for _ in range(length):
                    i, j, val = i + dir[0], j + dir[1], val + 1
                    spiral[i][j] = val
        return spiral
