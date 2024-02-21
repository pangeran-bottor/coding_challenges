from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        prev = prices[0]
        for price in prices:
            if price > prev:
                ans += price - prev
            prev = price
        return ans
