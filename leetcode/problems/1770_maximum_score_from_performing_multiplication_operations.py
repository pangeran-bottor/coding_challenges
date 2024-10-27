from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # from functools import cache
        # @cache
        # def dp(i, left, right):
        #     if i == len(multipliers):
        #         return 0

        #     return max(
        #         nums[left]*multipliers[i] + dp(i+1, left+1, right),
        #         nums[len(nums)-right-1]*multipliers[i] + dp(i+1, left, right+1)
        #     )

        # return dp(0, 0, 0)
        n, m = len(nums), len(multipliers)
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                mult = multipliers[i]
                right = n - (i - left) - 1
                dp[i][left] = max(
                    dp[i + 1][left + 1] + nums[left] * mult,
                    dp[i + 1][left] + nums[right] * mult,
                )
        return dp[0][0]
