from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        f(x) is the min cost to reach the top with len(cost) = 3

        10, 15, 20, 11

        f(0) = 0
        f(1) = 0
        f(2) = min(f(0) + cost[0], f(1) + cost[1]) = min(cost[0], cost[1]) = 10
        f(3) = min(f(1) + cost[1], f(2) + cost[2]) = min(15, 30) = 15
        f(4) = min(f(2) + cost[2], f(3) + cost[3]) = min(30, 26) = 26
        ....
        """
        n = len(cost)
        dp = [0 for _ in range(n + 1)]
        for x in range(2, n + 1):
            dp[x] = min(dp[x - 2] + cost[x - 2], dp[x - 1] + cost[x - 1])

        return dp[n]
