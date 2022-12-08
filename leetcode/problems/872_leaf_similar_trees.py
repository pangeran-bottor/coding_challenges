from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            leaves = []
            stack = [root]

            while stack:
                cur = stack.pop()
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)

                if not cur.left and not cur.right:
                    leaves.append(cur.val)
            return leaves

        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)
        return leaves1 == leaves2
