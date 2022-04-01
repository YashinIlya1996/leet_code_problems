""" https://leetcode.com/problems/counting-bits/ """
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0, 1]
        if n < 2:
            return answer[:n+1]
        next_2_pow = 2
        # Можно и не разделять текущую и следующую степень, но тогда в каждой итерации появится лишнее умножение
        current_2_pow = 1
        for i in range(2, n + 1):
            if i == next_2_pow:
                next_2_pow *= 2
                current_2_pow *= 2
            # Эта формула исходит из самой сути двоичной записи числа
            answer.append(1 + answer[i - current_2_pow])
        return answer


