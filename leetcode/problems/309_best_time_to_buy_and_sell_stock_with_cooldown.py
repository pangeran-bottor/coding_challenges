from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(curr_trx, is_hold):
            if (curr_trx, is_hold) in memo:
                return memo[(curr_trx, is_hold)]
            if curr_trx >= len(prices):
                return 0

            skip = dp(curr_trx + 1, is_hold)
            if is_hold:
                do = prices[curr_trx] + dp(curr_trx + 2, 0)
            else:
                do = -prices[curr_trx] + dp(curr_trx + 1, 1)

            memo[(curr_trx, is_hold)] = max(skip, do)
            return memo[(curr_trx, is_hold)]

        memo = {}
        return dp(0, 0)
