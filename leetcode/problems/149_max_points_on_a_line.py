import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_slope(point1, point2):
            x1, y1 = point1[0], point1[1]
            x2, y2 = point2[0], point2[1]
            if x1 == x2:
                return float("inf")
            return (y2 - y1) / (x2 - x1)

        n = len(points)
        if n <= 2:
            return n

        ans = 2
        for i in range(n):
            slope_count = collections.defaultdict(int)
            for j in range(n):
                if i == j:
                    continue

                slope = get_slope(points[i], points[j])
                slope_count[slope] += 1

            ans = max(ans, 1 + max(slope_count.values()))
        return ans
