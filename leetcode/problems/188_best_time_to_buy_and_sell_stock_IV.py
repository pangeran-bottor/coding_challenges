from functools import cache
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # n = len(prices)
        # dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n + 1)]

        # for i in range(n-1, -1, -1):
        #     for r in range(1, k + 1):
        #         for is_hold in range(2):
        #             skip = dp[i+1][r][is_hold]

        #             if is_hold:
        #                 do = prices[i] + dp[i+1][r-1][0]
        #             else:
        #                 do = -prices[i] + dp[i+1][r][1]

        #             dp[i][r][is_hold] = max(skip, do)

        # return dp[0][k][0]
        @cache
        def dp(curr_trx, remains, is_hold):
            if remains == 0 or curr_trx == len(prices):
                return 0

            skip = dp(curr_trx + 1, remains, is_hold)
            do = 0
            if is_hold:
                do = prices[curr_trx] + dp(curr_trx + 1, remains - 1, 0)
            else:
                do = -prices[curr_trx] + dp(curr_trx + 1, remains, 1)
            return max(skip, do)

        return dp(0, k, 0)
