from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if not root:
                return 0
            
            q = deque([root])
            depth = 0
            while q:
                depth += 1
                next_level = []
                for node in q:
                    if not node.left and not node.right:
                        return depth
                    
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                q = next_level
        
        ans = bfs(root)
        return ans
