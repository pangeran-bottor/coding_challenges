from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {node: -1 for node in range(n)}
        for node in range(n):
            if color[node] != -1:
                continue

            color[node] = 0
            stack = [node]
            while stack:
                curr_node = stack.pop()
                for neighbor in graph[curr_node]:
                    if color[neighbor] == color[curr_node]:
                        return False

                    if color[neighbor] == -1:
                        color[neighbor] = (color[curr_node] + 1) % 2
                        stack.append(neighbor)

        return True
