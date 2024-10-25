from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for curr in range(coin, amount + 1):
                dp[curr] = min(dp[curr], dp[curr - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
