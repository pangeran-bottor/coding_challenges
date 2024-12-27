from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def _insert(root, val):
            if not root:
                return TreeNode(val)
            if root.val < val:
                root.right = _insert(root.right, val)
            else:
                root.left = _insert(root.left, val)
            return root

        return _insert(root, val)
