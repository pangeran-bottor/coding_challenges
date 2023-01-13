import collections
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = collections.defaultdict(list)
        for idx, p in enumerate(parent):
            g[p].append(idx)

        self.ans = 1

        def dfs(node: int) -> int:
            if len(g[node]) == 0:
                return 1
            res = 1
            for next_node in g[node]:
                length_of_child = dfs(next_node)
                if s[node] != s[next_node]:
                    self.ans = max(self.ans, length_of_child + res)
                    res = max(res, length_of_child + 1)
            return res

        dfs(0)
        return self.ans
