"""https://leetcode.com/problems/score-of-parentheses/"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Проходим по s, запоминая количество открывающих скобок в happy_count.
        Если видим закрывающую, а перед ней была открывающая, то прибавляем к результату 2 ** (happy_count - 1),
            а happy_count уменьшаем на 1, т.к. эта пара скобок уже не будет умножать результат.
        Если перед ')' также была ')', то не учитываем в подсчете.
        """
        result = 0
        multiple_count = 1
        prev_happy = False
        for char in s:
            if char == '(':
                multiple_count *= 2
                prev_happy = True
            elif prev_happy:
                multiple_count //= 2
                result += multiple_count
                prev_happy = False
            else:
                prev_happy = False
                multiple_count //= 2
        return result

