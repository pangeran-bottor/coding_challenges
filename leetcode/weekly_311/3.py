# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


def preorder(root1, root2, lvl):
    if (root1 == None or root2 == None):
        return

    if (lvl % 2 == 0):
        t = root1.val
        root1.val = root2.val
        root2.val = t

    preorder(root1.left, root2.right, lvl + 1)
    preorder(root1.right, root2.left, lvl + 1)
    
    
def reverse_at_odd(root):
    preorder(root.left, root.right, 0)
    
    
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # TODO: revisit graph traversal with recursion
        reverse_at_odd(root)
        return root
