from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = defaultdict(list)
        for n1, n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            cost = 0
            for next_node in g[node]:
                cost += dfs(next_node)

            # cost > 0 means there is an apple underneath this node,
            # then include this node as the path to node 0.
            if cost > 0 or hasApple[node]:
                # if current node is 0, no need additional 1 cost
                if node == 0:
                    return cost
                return cost + 1
            return 0

        res = dfs(0)
        if res > 0:
            return 2 * res
        return 0
