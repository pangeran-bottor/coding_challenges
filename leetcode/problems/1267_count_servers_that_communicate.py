from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_counts = [0 for _ in range(m)]
        col_counts = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_counts[i] += 1
                    col_counts[j] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and max(row_counts[i], col_counts[j]) > 1:
                    ans += 1
        return ans
