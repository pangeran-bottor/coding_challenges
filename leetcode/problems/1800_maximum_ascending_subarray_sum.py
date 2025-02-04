from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_sum = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            ans = max(ans, curr_sum)
        return ans
