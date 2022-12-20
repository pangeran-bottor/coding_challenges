from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        edge_map = {}
        for i, keys in enumerate(rooms):
            edge_map[i] = keys

        def dfs(visited, edge_map, cur_node):
            visited.add(cur_node)
            for next_node in edge_map[cur_node]:
                if next_node not in visited:
                    dfs(visited, edge_map, next_node)

        dfs(visited, edge_map, 0)
        print(visited)
        return len(rooms) == len(visited)
