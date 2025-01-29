from typing import List


class Solution:
    cycle_start = -1

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def _dfs(node):
            visited.add(node)

            for next_node in adj.get(node, []):
                if next_node not in visited:
                    parent[next_node] = node
                    _dfs(next_node)
                elif self.cycle_start == -1 and parent[node] != next_node:
                    parent[next_node] = node
                    self.cycle_start = next_node

        adj: dict = {}
        for a, b in edges:
            adj[a] = adj.get(a, []) + [b]
            adj[b] = adj.get(b, []) + [a]

        n = len(adj)
        parent = [-1 for _ in range(n + 1)]
        visited: set = set()

        self.cycle_start = -1
        _dfs(1)

        cycle_nodes = set()
        node = self.cycle_start
        while True:
            cycle_nodes.add(node)
            node = parent[node]
            if node == self.cycle_start:
                break

        for a, b in edges[::-1]:
            if a in cycle_nodes and b in cycle_nodes:
                return [a, b]

        return []
