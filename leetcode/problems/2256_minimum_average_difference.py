from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0 for _ in range(n+2)]
        right = [0 for _ in range(n+2)]

        for i in range(n):
            left[i+1] = left[i] + nums[i]
            right[n-i] = right[n-i+1] + nums[n-i-1]
        
        ans = float("inf")
        idx = -1
        for i in range(n):
            cur_left = left[i+1] // (i+1)
            cur_right = right[i+2] // (n-(i+1)) if n-i-1 > 0 else 0

            cur_ans = abs(cur_left - cur_right)
            if cur_ans < ans:
                ans = cur_ans
                idx = i
        return idx
