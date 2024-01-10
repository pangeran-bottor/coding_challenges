from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur.val:
                continue

            if cur.left:
                stack.append(cur.left)
                graph[cur.val].append(cur.left.val)
                graph[cur.left.val].append(cur.val)
            if cur.right:
                stack.append(cur.right)
                graph[cur.val].append(cur.right.val)
                graph[cur.right.val].append(cur.val)

        level = [start]
        visited = set()
        ans = 0
        while level:
            tmp = []
            for node in level:
                visited.add(node)
                tmp.extend([el for el in graph[node] if el not in visited])
            level = list(tmp)
            ans += 1
        return ans - 1
