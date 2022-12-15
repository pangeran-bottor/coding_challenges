from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def traverse(edge_map, visited, node):
            if node in visited:
                return

            visited.add(node)
            for next_node in edge_map[node]:
                traverse(edge_map, visited, next_node)
            
        edge_map = defaultdict(list)
        visited = set()
        for n1, n2 in edges:
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)

        ans = 0
        for node in range(n):
            if node not in visited:
                traverse(edge_map, visited, node)
                ans += 1
        return ans
