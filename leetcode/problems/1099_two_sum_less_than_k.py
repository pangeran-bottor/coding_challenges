from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1
        nums.sort()
        
        left, right = 0, len(nums)-1
        
        max_sum = sum(nums[:2])
        if max_sum >= k:
            return -1
        
        while left < right:
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                max_sum = max(max_sum, nums[left] + nums[right])
                left += 1
        
        return max_sum
