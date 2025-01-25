from collections import deque
from typing import Deque, List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        flags = [False for _ in range(n)]

        in_degree = [0 for _ in range(n)]
        adj: List[List[int]] = [[] for _ in range(n)]

        for idx, neighbors in enumerate(graph):
            for neighbor in neighbors:
                adj[neighbor].append(idx)
                in_degree[idx] += 1

        q: Deque = deque()
        for idx, degree in enumerate(in_degree):
            if degree == 0:
                q.append(idx)

        while q:
            curr_node = q.popleft()
            flags[curr_node] = True
            for neighbor in adj[curr_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return [idx for idx, val in enumerate(flags) if val]
