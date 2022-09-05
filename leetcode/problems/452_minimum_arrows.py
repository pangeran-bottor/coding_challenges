from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        N = len(points)
        ans = 1
        
        for i in range(N-1):
            if points[i+1][0] > points[i][1]:
                ans += 1
                continue
            
            points[i+1] = [points[i+1][0], points[i][1]]
        return ans
