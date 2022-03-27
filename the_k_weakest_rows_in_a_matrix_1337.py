""" https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/ """
from typing import List
from operator import itemgetter


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power_dict = {num: row.index(0) if 0 in row else len(row) for num, row in enumerate(mat)}
        return [x[0] for x in sorted(power_dict.items(), key=itemgetter(1))][:k]

