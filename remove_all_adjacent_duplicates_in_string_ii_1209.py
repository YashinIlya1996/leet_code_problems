""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/ """


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        if len(s) < k:
            return s
        else:
            def _remove_duplicates(s: str, k: int, d: list[int]) -> str:
                pos = 0
                _s = ''
                for el in d:
                    _s = s.replace(s[el:el + k], '')
                return _s

            duplicates_position = []
            cursor = 0
            stop_position = len(s) - k
            while True:
                while cursor <= stop_position:
                    if (s[cursor] == s[cursor + 1]) and (len(set(s[cursor:cursor + k])) == 1):
                        duplicates_position.append(cursor)
                        cursor += k
                    else:
                        cursor += 1
                if not duplicates_position:
                    break
                else:
                    s = _remove_duplicates(s, k, duplicates_position)
                    duplicates_position = []
                    stop_position = len(s) - k
                    cursor = 0
        return s


if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    print(Solution().removeDuplicates(s, k))
