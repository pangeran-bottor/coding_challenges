from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        N = len(grid)
        for i in range(N-2):
            ans.append([])
            for j in range(N-2):
                el = 0
                for row in range(3):
                    for col in range(3):
                        el = max(el, grid[i+row][j+col])
                ans[-1].append(el)
        return ans
