""" https://leetcode.com/problems/valid-palindrome-ii/ """


class Solution:
    def validPalindrome(self, s: str) -> bool:
        head, tail = 0, len(s) - 1

        while head <= tail:
            if s[head] != s[tail]:
                s1 = s[head:tail]
                s2 = s[head + 1: tail + 1]
                return s1 == s1[::-1] or s2 == s2[::-1]
            head, tail = head + 1, tail - 1
        return True
