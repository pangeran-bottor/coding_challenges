from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for idx, num in enumerate(nums):
            cur_max = 0
            for i in range(idx):
                if nums[i] < nums[idx]:
                    cur_max = max(cur_max, dp[i])
            dp[idx] = cur_max + 1
        return max(dp)
