from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        paths = []

        def backtrack(cur_node, path):
            if cur_node == target:
                paths.append(list(path))
                return

            for next_node in graph[cur_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        path = [0]
        backtrack(0, path)
        return paths
