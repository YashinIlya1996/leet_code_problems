""" https://leetcode.com/problems/partition-labels/ """

from typing import List
from collections import Counter


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        primary_counter = Counter(s)
        answer = []
        current_set = set()
        current_num = 0
        for char in s:
            current_set.add(char)
            primary_counter[char] -= 1
            current_num += 1
            if not primary_counter[char]:
                current_set.remove(char)
            if all([not primary_counter[ch] for ch in current_set]):
                answer.append(current_num)
                current_num = 0
                current_set.clear()
        if current_num:
            answer.append(current_num)
        return answer


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))