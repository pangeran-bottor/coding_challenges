from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        rows = [root] if root else []

        while rows:
            ans.append(max([node.val for node in rows if node]))
            next_rows = []
            for node in rows:
                if node.left:
                    next_rows.append(node.left)
                if node.right:
                    next_rows.append(node.right)
            rows = next_rows

        return ans
