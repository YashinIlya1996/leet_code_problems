""" https://leetcode.com/problems/01-matrix/ """


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        fillval = max(m, n)
        res = [[fillval for _ in range(n)] for _ in range(m)]
        to_next_handle = set()
        not_handled = {(i, j) for i in range(m) for j in range(n)}
        steps = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def add_to_next_handle(i_, j_, nh: set):
            for di, dj in steps:
                if (coord := (i_ + di, j_ + dj)) in not_handled:
                    nh.add(coord)

        def get_min(i_, j_):
            min_ = fillval + 1
            for di, dj in steps:
                ci, cj = i_ + di, j_ + dj
                if ci < 0 or cj < 0 or ci >= m or cj >= n:
                    continue
                min_ = min(res[ci][cj] + 1, min_)
            return min_

        # initialization
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    not_handled -= {(i, j)}
                    to_next_handle -= {(i, j)}
                    add_to_next_handle(i, j, to_next_handle)

        while to_next_handle:
            next_iter_set = set()
            for _ in range(len(to_next_handle)):
                i, j = to_next_handle.pop()
                res[i][j] = get_min(i, j)
                not_handled -= {(i, j)}
                add_to_next_handle(i, j, next_iter_set)
            to_next_handle.update(next_iter_set)

        return res


if __name__ == '__main__':
    testcases = (
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1], [0, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1], [0, 1, 2], [1, 2, 3]]),
    )
    for solution_class in (Solution,):
        print(f'Testing {solution_class.__name__}')
        for data, expected in testcases:
            value = solution_class().updateMatrix(data)
            res = 'Success!' if value == expected else 'FAILED'
            print(f'{res:<10} data = {str(data):<50} expected = {str(expected):<10} value = {str(value):<10}')
        print('-' * 120)
