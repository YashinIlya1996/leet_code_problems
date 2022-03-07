from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __str__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        elif list2 is None and list1 is not None:
            return list1
        elif all([list1 is None, list2 is None]):
            return None
        else:
            if list1.val <= list2.val:
                min_node = list1
                list1 = list1.next
            else:
                min_node = list2
                list2 = list2.next
            root = min_node
            current = root
            while all([list1 is not None, list2 is not None]):
                if list1.val <= list2.val:
                    min_node = list1
                    list1 = list1.next
                else:
                    min_node = list2
                    list2 = list2.next
                current.next = min_node
                current = current.next
            if list1 is None:
                current.next = list2
            else:
                current.next = list1
            return root
