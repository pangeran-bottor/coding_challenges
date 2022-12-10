from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []

        def tree_sum(root):
            if not root:
                return 0

            left_sum = tree_sum(root.left)
            right_sum = tree_sum(root.right)
            total = left_sum + root.val + right_sum

            subtree_sums.append(total)
            return total
        
        total = tree_sum(root)

        max_val = 0
        print(subtree_sums)
        for s in subtree_sums:
            max_val = max(max_val, s * (total-s))
        
        return max_val % (10**9 + 7)
