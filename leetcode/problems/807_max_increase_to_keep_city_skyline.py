from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += (min(
                    max(grid[i]),
                    max([row[j] for row in grid])
                ) - grid[i][j])
        return ans
