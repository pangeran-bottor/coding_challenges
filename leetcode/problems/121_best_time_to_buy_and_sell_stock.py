from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(lowest, price)
            result = max(result, price-lowest)
        return result
