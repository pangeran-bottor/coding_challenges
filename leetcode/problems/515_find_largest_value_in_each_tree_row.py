from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque([(root, 1)])
        while queue:
            curr_node, level = queue.popleft()
            if not curr_node:
                continue
            if level > len(ans):
                ans.append(curr_node.val)
            else:
                ans[level - 1] = max(curr_node.val, ans[level - 1])

            if curr_node.left:
                queue.append((curr_node.left, level + 1))
            if curr_node.right:
                queue.append((curr_node.right, level + 1))
        return ans
