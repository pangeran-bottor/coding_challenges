from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        cur_sum = 0
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            ans = max(ans, cur_sum)
        return ans
