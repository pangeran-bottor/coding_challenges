from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        ans = 1

        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i - 1] > nums[i]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            ans = max(ans, inc, dec)
        return ans
