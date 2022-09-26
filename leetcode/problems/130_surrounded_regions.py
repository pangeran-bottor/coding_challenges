from typing import List


class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        TODO: implementation using BFS for learning purpose.
        """
        def dfs(i, j, grid):
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] != "O":
                return
            grid[i][j] = "#"
            for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dfs(i+r, j+c, grid)
        
        R, C = len(grid), len(grid[0])
        
        for col in range(C):
            if grid[0][col] == "O":
                dfs(0, col, grid)
            if grid[R-1][col] == "O":
                dfs(R-1, col, grid)
        
        for row in range(R):
            if grid[row][0] == "O":
                dfs(row, 0, grid)
            if grid[row][C-1] == "O":
                dfs(row, C-1, grid)
        
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "#":
                    grid[i][j] = "O"
