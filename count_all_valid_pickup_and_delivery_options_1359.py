""" https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/ """

from math import factorial


class Solution:
    def countOrders(self, n: int) -> int:
        return (factorial(2 * n) // 2 ** n) % (10 ** 9 + 7)
