from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r, c, grid):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return
            if grid[r][c] != 1:
                return

            grid[r][c] = 0
            for i, j in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                dfs(i, j, grid)

        m, n = len(grid), len(grid[0])
        for i in range(n):
            dfs(0, i, grid)
            dfs(m - 1, i, grid)
        for j in range(m):
            dfs(j, 0, grid)
            dfs(j, n - 1, grid)

        ans = 0
        for row in grid:
            ans += sum(row)
        return ans
