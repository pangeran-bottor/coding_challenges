from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        d = [[float("inf") for j in range(C)] for i in range(R)]
        pq = [(0, 0, 0)]
        d[0][0] = 0

        while pq:
            cost, r, c = heappop(pq)

            if (r, c) == (R - 1, C - 1):
                return cost

            cur_pq = []
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    ncost = max(cost, abs(heights[r][c] - heights[nr][nc]))
                    if ncost < d[nr][nc]:
                        d[nr][nc] = ncost
                        heappush(pq, (d[nr][nc], nr, nc))
