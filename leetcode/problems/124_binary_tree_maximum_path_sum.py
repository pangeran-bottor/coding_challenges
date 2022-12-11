from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def get_max(root):
            nonlocal ans
            if not root:
                return 0

            left_max = max(get_max(root.left), 0)
            right_max = max(get_max(root.right), 0)

            ans = max(ans, left_max + root.val + right_max)
            return max(left_max + root.val, right_max + root.val)

        get_max(root)
        return ans
