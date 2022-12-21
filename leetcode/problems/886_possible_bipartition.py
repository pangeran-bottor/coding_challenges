import collections
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in edge_map[node]:
                if color[neighbor] == color[node]: return False
                if color[neighbor] == -1:
                    # red to blue, or vice versa
                    if not dfs(neighbor, 1 - node_color):
                        return False
            return  True

        edge_map = collections.defaultdict(list)
        for n1, n2 in dislikes:
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)


        # -1 -> no color
        #  0 -> red
        #  1 -> blue

        color = [-1 for _ in range(n+1)]
        for i in range(1, n+1):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False

        return True
