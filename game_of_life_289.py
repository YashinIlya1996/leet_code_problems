""" https://leetcode.com/problems/game-of-life/ """
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        row_count, col_count = len(board), len(board[0])
        mask = [list() for _ in range(row_count)]

        def count_neighbours(i, j):
            """ Возвращает количество 'живых' соседей вокруг клетки [i][j] """
            live_counter = 0
            row_start = max(0, i - 1)
            row_stop = min(row_count - 1, i + 1)
            col_start = max(0, j - 1)
            col_stop = min(col_count - 1, j + 1)

            for row in board[row_start:row_stop + 1]:
                for cell in row[col_start: col_stop + 1]:
                    if cell:
                        live_counter += 1

            if board[i][j]:
                live_counter -= 1

            return live_counter

        # mask - лист, хранящий количество живых клеток вокруг клетки [i][j] для всей доски
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                mask[i].append(count_neighbours(i, j))

        # Обновление доски
        for i, row in enumerate(mask):
            for j, cell in enumerate(row):
                board[i][j] = 0 if cell < 2 else 1 if cell == 3 else 0 if cell > 3 else board[i][j]
