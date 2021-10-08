from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        for i in range(len(points)-1):
            ans = max(points[i+1][0]-points[i][0], ans)
        return ans
