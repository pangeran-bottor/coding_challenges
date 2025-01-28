from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def _dfs(r, c):
            if grid[r][c] == 0:
                return 0

            val = grid[r][c]
            grid[r][c] = 0
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc):
                    val += _dfs(nr, nc)
            return val

        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(ans, _dfs(i, j))
        return ans
