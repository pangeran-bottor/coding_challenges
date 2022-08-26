from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        N = len(nums)
        return N*(N+1)//2 - nums_sum
