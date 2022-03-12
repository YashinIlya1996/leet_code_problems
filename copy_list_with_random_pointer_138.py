"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    # def __str__(self):
    #     if self.random:
    #         return f'{self.val} -> {self.next} ({self.random.val})'
    #     return f'{self.val} -> {self.next}'


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        answer = head
        if head:
            nodes_list = [] # TODO change list to dict would be faster
            new_nodes = []
            tracking_node = head
            num = 0
            while tracking_node:
                tracking_node.position = num
                num += 1
                nodes_list.append(tracking_node)
                new_nodes.append(Node(tracking_node.val))
                tracking_node = tracking_node.next

            num = 0
            for old, new in zip(nodes_list, new_nodes):
                if old.random:
                    new.random = new_nodes[old.random.position]
                if old.next:
                    new.next = new_nodes[num + 1]


            answer = new_nodes[0]
        return answer


head = [Node(7),
        Node(13),
        Node(11),
        Node(10),
        Node(1),
        ]

head[0].next = head[1]
head[1].next = head[2]
head[1].random = head[0]
head[2].next = head[3]
head[2].random = head[4]
head[3].next = head[4]
head[3].random = head[2]
head[4].random = head[0]

c = Solution().copyRandomList(head[0])
