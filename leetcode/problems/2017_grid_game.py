from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
            grid[1][n - i - 1] += grid[1][n - i]

        ans = float("inf")
        for i in range(n):
            second_robot = max(grid[0][n - 1] - grid[0][i], grid[1][0] - grid[1][i])
            ans = min(ans, second_robot)
        return ans
