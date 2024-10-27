from collections import defaultdict
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        for num in nums:
            points[num] += num
        elements = sorted(points.keys())

        n = len(elements)
        dp = [0 for _ in range(n + 1)]
        dp[1] = points[elements[0]]

        for i in range(2, n + 1):
            if elements[i - 1] == elements[i - 2] + 1:
                dp[i] = max(dp[i - 2] + points[elements[i - 1]], dp[i - 1])
            else:
                dp[i] = dp[i - 1] + points[elements[i - 1]]

        return dp[n]
