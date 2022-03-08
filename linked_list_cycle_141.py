""" https://leetcode.com/problems/linked-list-cycle/ """

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        self.viewed = True
        if not hasattr(self.next, 'viewed'):
            return f'{self.val} -> {self.next}'
        else:
            return f'{self.val} -> cycle to {self.next.val}'


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current is not None and not hasattr(current, 'viewed'):
            current.viewed = True
            current = current.next
        return hasattr(current, 'viewed')
