from collections import deque
from typing import Dict, List, Set, Tuple


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        def _bfs(course):
            queue = deque([course])
            while queue:
                curr_node = queue.popleft()
                for next_node in adj.get(curr_node, []):
                    if (course, next_node) in visited:
                        continue
                    prereq_tab[course][next_node] = True
                    visited.add((course, next_node))
                    queue.append(next_node)

        adj: Dict[int, List[int]] = {}
        for pre, course in prerequisites:
            if pre not in adj:
                adj[pre] = []
            adj[pre].append(course)

        prereq_tab = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        visited: Set[Tuple[int, int]] = set()
        for course in range(numCourses):
            _bfs(course)

        ans = []
        for start, target in queries:
            ans.append(prereq_tab[start][target])
        return ans
