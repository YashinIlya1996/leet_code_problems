""" https://leetcode.com/problems/3sum-with-multiplicity/ """
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        """ Переопределение элементов arr и target тождественно равно искомому значению, но избавляет от необходимости
            следить за возможным повторением нулей в ответе и, как следствие, завышением ответа,
            а также сокращает используемую память, сокращая длину списка, т.к. arr[i] >= target не изменяют количество
            возможных комбинаций, и, как следствие, ответ"""
        arr = [el + 1 for el in arr]
        target += 3
        arr = [el for el in arr if el < target]

        max_in_arr = max(arr)
        memo_arr = [[0 for _ in range(max_in_arr + 1)]]
        """ memo_arr[i][j] - сколько элементов j есть в подсписке arr[i:] """
        for i in arr:
            memo_arr[0][i] += 1
        for i in range(len(arr) - 1):
            memo_arr.append(memo_arr[-1].copy())
            memo_arr[-1][arr[i]] -= 1

        memo_2sum = [[0 for _ in range(target + 1)] for _ in range(len(arr) - 1)]
        """ memo_2sum[i][j] = количество способов, которыми можно составить число j 
            в подсписке arr[i:] суммой двух элементов из arr[i:] """
        last = arr[-1] + arr[-2]
        memo_2sum[-1] = [1 if i == last else 0 for i in range(target + 1)]
        for i in range(len(arr) - 3, -1, -1):
            for j in range(target + 1):
                additional = memo_arr[i + 1][j - arr[i]] if 0 <= j - arr[i] <= max_in_arr else 0
                memo_2sum[i][j] = memo_2sum[i + 1][j] + additional

        answer = 0
        for num, i in enumerate(arr[:-2]):
            answer += memo_2sum[num + 1][target - i]
        return answer % mod

