""" https://leetcode.com/problems/swapping-nodes-in-a-linked-list/ """
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        k_head = head
        for _ in range(1, k):
            k_head = k_head.next
        k_tail, tail = head, k_head
        while tail.next is not None:
            k_tail, tail = k_tail.next, tail.next
        k_head.val, k_tail.val = k_tail.val, k_head.val
        return head
