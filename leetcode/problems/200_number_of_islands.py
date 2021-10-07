from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid):
            if i < 0 or i >= len(grid) or \
               j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                return

            grid[i][j] = "#"
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni = i + dx
                nj = j + dy
                dfs(ni, nj, grid)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j, grid)
        return count
