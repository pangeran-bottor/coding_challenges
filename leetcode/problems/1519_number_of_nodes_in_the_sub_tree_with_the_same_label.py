import collections
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = collections.defaultdict(list)
        for n1, n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        label_counts = {}
        for ch in "abcdefghijklmnopqrstuvwxyz":
            label_counts[ch] = 0

        ans = [0 for _ in range(n)]

        def dfs(node, parent):
            prev = label_counts[labels[node]]
            label_counts[labels[node]] += 1
            for next_node in g[node]:
                if next_node != parent:
                    dfs(next_node, node)

            ans[node] = label_counts[labels[node]] - prev

        dfs(0, -1)
        return ans
