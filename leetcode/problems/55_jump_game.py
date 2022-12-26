from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if len(nums) > 1 and nums[0] == 0: return False

        n = len(nums)
        target = n-1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= target:
                target = i
        return target == 0
