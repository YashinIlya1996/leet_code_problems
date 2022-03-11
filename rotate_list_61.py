""" https://leetcode.com/problems/rotate-list/ """

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            length, tail, old_head = 1, head, head
            while tail.next:
                length += 1
                tail = tail.next
            offset = k % length
            if offset == 0:
                return head
            for _ in range(1, length - offset):
                head = head.next
            new_head = head.next
            head.next = None
            tail.next = old_head

            return new_head
        return head
