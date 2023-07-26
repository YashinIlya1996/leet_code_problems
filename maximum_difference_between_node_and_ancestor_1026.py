""" https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/ """

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.__class__.__name__}({self.val, self.left, self.right})'


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_diff = 0

        def find_diff(min_: int, max_: int, node: Optional[TreeNode]) -> None:
            nonlocal max_diff
            max_diff = max(max_diff, abs(min_ - max_))
            if node.left is not None:
                find_diff(min(min_, node.left.val), max(max_, node.left.val), node.left)
            if node.right is not None:
                find_diff(min(min_, node.right.val), max(max_, node.right.val), node.right)
        find_diff(root.val, root.val, root)
        return max_diff


if __name__ == '__main__':
    tree = TreeNode(
        8,
        TreeNode(3,
                 TreeNode(1),
                 TreeNode(6,
                          TreeNode(4),
                          TreeNode(7))),
        TreeNode(10, None, TreeNode(14, TreeNode(13))))
    a = Solution().maxAncestorDiff(tree)
    breakpoint()
