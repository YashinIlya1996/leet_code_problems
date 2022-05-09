""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/ """


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        import re
        pattern = r'((.)\2{' + str(k - 1) + '})'
        pattern = re.compile(pattern)
        match = re.fullmatch(pattern, s)
        while match:
            duplicates = [c[0] for c in match]
            for duplicate in duplicates:
                s = s.replace(duplicate, '')
            match = re.findall(pattern, s)
        return s

if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    print(Solution().removeDuplicates(s, k))
