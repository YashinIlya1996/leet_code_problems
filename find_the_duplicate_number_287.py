""" https://leetcode.com/problems/find-the-duplicate-number/ """
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ Можно также решить отсортировав массив и применив бинарный поиск, но тогда время выполнения
            увеличится до сортировки O(N logN). Применяем хэш-таблицу.
            Сразу создать лист с индексами == значениями элементов в исходном листе
            оказалось быстрее по времени выполнения чем решение через словарь. """
        hash_table = [False for _ in range(len(nums))]
        for num in nums:
            if hash_table[num]:
                return num
            hash_table[num] = True
