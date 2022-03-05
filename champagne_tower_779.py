from typing import List


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # def champagneTower(self):
        class Node:
            def __init__(self, row, glass):
                self.position = row, glass
                self.left = row + 1, glass
                self.right = row + 1, glass + 1
                self.value = 0
                self.parents_count = 1 if any([row == glass, glass == 0]) else 2
                # TODO Добавить метод add(), который увеличивает value, а если оно превышает 1, вызывает add() для детей
                # TODO изменить структуру на древовидную
                # TODO избавиться от лишних полей, добавить @property filled: bool

            def __str__(self):
                return f'{self.position}, v: {self.value}'

        # tower = [] #Node
        tower: List[List[Node]] = []
        for num in range(100):
            row = [Node(num, glass) for glass in range(num + 1)]
            tower.append(row)

        cur_filling_glasses: List[Node] = [tower[0][0]]
        stream_count = 1

        for i in range(poured):
            future_filling_glasses = []
            future_stream_count = stream_count
            adding_part = 1 / stream_count
            for glass in cur_filling_glasses:
                glass.value += adding_part
                if round(glass.value, 5) >= 1:
                    while glass in cur_filling_glasses:
                        cur_filling_glasses.remove(glass)
                    future_stream_count += 2 - glass.parents_count
                    future_filling_glasses.append(tower[glass.left[0]][glass.left[1]])
                    future_filling_glasses.append(tower[glass.right[0]][glass.right[1]])

            cur_filling_glasses.extend(future_filling_glasses)
            stream_count = future_stream_count

        return tower[query_row][query_glass].value


print(Solution().champagneTower(*map(int, input().split())))
