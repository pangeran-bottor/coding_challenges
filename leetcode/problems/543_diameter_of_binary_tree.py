from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def _height(root):
            if not root:
                return 0

            left = _height(root.left)
            right = _height(root.right)
            self.diameter = max(self.diameter, 1 + left + right)
            return 1 + max(left, right)

        _height(root)
        return self.diameter - 1
