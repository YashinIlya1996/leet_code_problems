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
            if all([el > 1 for el in c.values()]):
                return None
            root = ListNode()
            answer = root
            current = head
            while True:
                while c[current.val] != 1:
                    current = current.next
                    if current is None:
                        root.next = None
                        return answer.next
                root.next = current
                root = root.next
                current = current.next
                if root is None or current is None:
                    break
            return answer.next


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
def list_to_nodes(l: list):
    root = ListNode()
    cur = root
    for el in l:
        cur.next = ListNode(el)
        cur = cur.next
    return root.next


print(Solution().deleteDuplicates(list_to_nodes([2, 3, 3])))
