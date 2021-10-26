from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount+1):
            if dp[i] >= 0:
                continue
            min_changes = float("inf")
            min_c = -1
            for coin in coins:
                if i - coin >= 0:
                    if 0 <= dp[i-coin] < min_changes:
                        min_changes = dp[i-coin]
                        min_c = coin

            if min_c != -1:
                dp[i] = min_changes + 1

        return dp[amount]
