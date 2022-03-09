""" https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ """
from typing import Optional
from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    def __str__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            c = Counter()
            node = head
            while node:
                c[node.val] += 1
                node = node.next
            a = sorted([el[0] for el in c.items() if el[1] == 1])
            root = ListNode()
            current = root
            for el in a:
                current.next = ListNode(el)
                current = current.next
            return root.next
        return head


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
def list_to_nodes(l: list):
    root = ListNode()
    cur = root
    for el in l:
        cur.next = ListNode(el)
        cur = cur.next
    return root.next


print(Solution().deleteDuplicates(list_to_nodes([1, 2, 3, 3, 4, 4, 5])))
