from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(1, N):
            grid[0][i] += grid[0][i-1]
        for j in range(1, M):
            grid[j][0] += grid[j-1][0]
        
        for i in range(1, M):
            for j in range(1, N):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[M-1][N-1]
