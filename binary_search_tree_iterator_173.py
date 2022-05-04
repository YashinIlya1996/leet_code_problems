""" https://leetcode.com/problems/binary-search-tree-iterator/ """
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.lst = []

    def _to_list(self, root):


    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
