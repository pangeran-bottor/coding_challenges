from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ans = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root, min_acs, max_acs):
            if not root:
                return

            tmp_min = abs(root.val - min_acs)
            tmp_max = abs(root.val - max_acs)
            self.ans = max(self.ans, tmp_min, tmp_max)

            traverse(root.left, min(root.val, min_acs), max(root.val, max_acs))
            traverse(root.right, min(root.val, min_acs), max(root.val, max_acs))

        traverse(root, root.val, root.val)
        return self.ans
