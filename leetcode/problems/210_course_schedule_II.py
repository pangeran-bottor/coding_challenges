from typing import List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):
            if in_stack[node]:
                return True

            in_stack[node] = True
            for next_node in adj[node]:
                if in_stack[next_node]:
                    return True
                if next_node not in visited:
                    dfs(next_node)

            visited.add(node)
            in_stack[node] = False
            s.append(node)
            return False

        visited: Set[int] = set()
        in_stack = [False for _ in range(numCourses)]
        s: List[int] = []
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        for pre, course in prerequisites:
            adj[course].append(pre)

        for course in range(numCourses):
            if course not in visited:
                if dfs(course):
                    return []

        return s[::-1]
