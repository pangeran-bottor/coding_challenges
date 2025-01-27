from collections import deque
from typing import Dict, List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj: Dict[int, List[int]] = {}
        for n1, n2 in edges:
            if n1 not in adj:
                adj[n1] = []
            if n2 not in adj:
                adj[n2] = []
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        queue = deque([source])
        while queue:
            curr_node = queue.popleft()
            if curr_node in visited:
                continue
            if curr_node == destination:
                return True

            visited.add(curr_node)
            for next_node in adj.get(curr_node, []):
                if next_node not in visited:
                    queue.append(next_node)
        return False
