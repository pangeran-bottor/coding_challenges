import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        edge_map = collections.defaultdict(list)
        for n1, n2 in edges:
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)
        
        def dfs(visited, edge_map, cur_node, target):
            if cur_node == target:
                return True
            
            visited.add(cur_node)
            for next_node in edge_map[cur_node]:
                if next_node not in visited:
                    if dfs(visited, edge_map, next_node, target):
                        return True
            return False

        return dfs(visited, edge_map, source, destination)
