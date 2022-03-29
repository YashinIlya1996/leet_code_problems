""" https://leetcode.com/problems/is-subsequence/ """


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        pointer, last_index = 0, len(s) - 1
        for char in t:
            if char == s[pointer]:
                if pointer == last_index:
                    return True
                else:
                    pointer += 1
        return False
