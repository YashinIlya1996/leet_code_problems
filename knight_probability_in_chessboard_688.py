""" https://leetcode.com/problems/knight-probability-in-chessboard/ """
from functools import cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        stak_len = 0
        steps = ((-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1))
        max_position = n - 1
        out_cache = {}
        next_cache = {}
        rec_cache = {}

        def is_outboarded(point: tuple[int, int]) -> bool:
            if point in out_cache:
                return out_cache[point]
            x, y = point
            result = any((x < 0, y < 0, x > max_position, y > max_position))
            out_cache[point] = result
            return result

        def next_positions(point: tuple[int, int]):
            if point in next_cache:
                return next_cache[point]
            x, y = point
            next_pos = [p for dx, dy in steps if not is_outboarded((p := (x + dx, y + dy)))]
            next_cache[point] = next_pos
            return next_pos

        def recursive(point: tuple[int, int], depth=0):
            if (key := (point, depth)) in rec_cache:
                return rec_cache[key]
            nonlocal stak_len
            if depth == k:
                return 1
            else:
                res = sum(recursive(p, depth + 1) for p in next_positions(point))
                rec_cache[(point, depth)] = res
                return res

        return recursive((row, column)) / (8 ** k)


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        stak_len = 0
        steps = ((-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1))
        max_position = n - 1

        @cache
        def is_outboarded(point: tuple[int, int]) -> bool:
            x, y = point
            return any((x < 0, y < 0, x > max_position, y > max_position))

        @cache
        def next_positions(point: tuple[int, int]):
            x, y = point
            return [p for dx, dy in steps if not is_outboarded((p := (x + dx, y + dy)))]

        @cache
        def recursive(point: tuple[int, int], depth=0):
            nonlocal stak_len
            if depth == k:
                return 1
            else:
                return sum(recursive(p, depth + 1) for p in next_positions(point))

        return recursive((row, column)) / (8 ** k)


if __name__ == '__main__':
    n, k = 3, 3
    x, y = 0, 0
    print(Solution().knightProbability(n, k, 0, 0))
    # print(Solution().knightProbability(3, 1, 1, 2))
    # print(Solution().knightProbability(3, 1, 2, 1))
