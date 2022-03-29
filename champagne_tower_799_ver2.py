""" https://leetcode.com/problems/champagne-tower/ """


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0 for _ in range(i)] for i in range(1, 102)]
        tower[0][0] = poured

        def pour_glass(row, glass):
            """ Переливает излишки шампанского из стакана в нижележащие стаканы """
            nonlocal tower
            if tower[row][glass] > 1:
                half_overage = (tower[row][glass] - 1) / 2
                tower[row][glass] = 1
                tower[row + 1][glass] += half_overage
                tower[row + 1][glass + 1] += half_overage

        for num_row in range(len(tower)):
            for num_glass in range(len(tower[num_row])):
                pour_glass(num_row, num_glass)
                if num_row == query_row and num_glass == query_glass:
                    return tower[num_row][num_glass]
