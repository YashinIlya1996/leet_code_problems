""" https://leetcode.com/problems/remove-duplicate-letters/ """


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                counter[char] -= 1
            else:
                while stack and (stack[-1] > char and counter[stack[-1]] >= 1) and char not in stack:
                    del stack[-1]
                if char not in stack:
                    stack.append(char)
                counter[char] -= 1
        return "".join(stack)


