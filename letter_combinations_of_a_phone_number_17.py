""" https://leetcode.com/problems/letter-combinations-of-a-phone-number/ """
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        from itertools import product

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        p = product(*[mapping[d] for d in digits])
        answer = []
        for t in p:
            answer.append(''.join(t))

        return answer
