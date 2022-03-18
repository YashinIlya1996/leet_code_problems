""" https://leetcode.com/problems/remove-duplicate-letters/ """


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        """
            counter - словарь, который хранит количество символов оставшихся в строке и состояние символа
        (есть он в стэке на данный момент или нет). Хранение состояния в counter сильно ускоряет время работы
        по сравнению с проверкой наличия в стэке через char in stack и приближает решение к O(n)
        """

        counter = {}
        for char in s:
            counter[char] = [counter.get(char, (0, False))[0] + 1, False]

        stack = []
        for char in s:
            """ Если первый символ - добавляем в стэк и обновляем counter """
            if not stack:
                stack.append(char)
                counter[char][0] -= 1
                counter[char][1] = True
            else:
                """ 
                    Иначе для соблюдения лексикографического порядка, нужно удалить из стэка символы,
                которые нарушают этот порядок, и которые ещё есть дальше в строке.
                    Если символ уже есть в стэке - значит порядок соблюден.
                """
                while stack and (stack[-1] > char and counter[stack[-1]][0] >= 1) and not counter[char][1]:
                    counter[stack[-1]][1] = False
                    del stack[-1]
                if not counter[char][1]:
                    stack.append(char)
                    counter[char][1] = True
                counter[char][0] -= 1  # Не забываем обновлять состояние символа и ранее удаленных.

        return "".join(stack)
