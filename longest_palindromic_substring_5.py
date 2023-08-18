""" https://leetcode.com/problems/longest-palindromic-substring/ """


class Solution:
    def longestPalindrome(self, s: str):
        if not s:
            return ""

        memo = [[True if i == j else False for i in range(len(s))] for j in range(len(s))]
        max_pal = s[0]
        for i in range(len(s) - 1):
            memo[i + 1][i] = s[i] == s[i + 1]
            if memo[i + 1][i]:
                max_pal = s[i:i + 2]

        for i in range(2, len(s)):
            for j in range(i - 1):
                res = memo[i - 1][j + 1] and (s[i] == s[j])
                memo[i][j] = res
                if res and (i - j + 1) > len(max_pal):
                    max_pal = s[j:i + 1]
        return max_pal


if __name__ == '__main__':
    s = "aaaa"
    print(Solution().longestPalindrome(s))
