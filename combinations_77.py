""" https://leetcode.com/problems/combinations/ """


class Solution:
    accum = []

    def combine(self, n: int, k: int) -> list[list[int]]:
        self.accum = []

        def _add_next(start: int, cur: list[int]):
            if len(cur) == k:
                self.accum.append(cur[:])
                return
            for i in range(start, n + 1):
                cur.append(i)
                _add_next(i + 1, cur)
                cur.pop()

        _add_next(1, [])
        return self.accum


if __name__ == '__main__':
    test_data = (
        ([1, 1], [[1]]),
        ([4, 2], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
    )
    for args, expected in test_data:
        assert Solution().combine(*args) == expected
