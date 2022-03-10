""" https://leetcode.com/problems/add-two-numbers/ """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        current = root
        appendix = 0
        while l1 or l2:
            current.next = ListNode()
            current = current.next
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            value = v1 + v2 + appendix
            appendix = value // 10
            current.val = value % 10
        if appendix:
            current.next = ListNode(appendix)
        return root.next