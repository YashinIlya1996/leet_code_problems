""" https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/ """


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        from string import ascii_lowercase
        length = 26
        answer = []
        while True:
            if k == n:
                answer.extend(['a'] * n)
                break
            else:
                n -= 1
                ind = k - n if k - n < length else length
                k -= ind
                answer.append(ascii_lowercase[ind - 1])

        return "".join(answer[::-1])
