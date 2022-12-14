from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)

        prev_prev = 0
        prev = nums[0]
        ans = 0

        for i in range(1, n):
            cur = max(nums[i] + prev_prev, prev)
            ans = max(ans, cur)

            prev_prev = prev
            prev = cur

        return ans
