from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [1] * N

        multiplier = 1
        for i in range(1, N):
            multiplier *= nums[i-1]
            result[i] *= multiplier
        
        multiplier = 1
        for i in range(N-2, -1, -1):
            multiplier *= nums[i+1]
            result[i] *= multiplier


        return result
