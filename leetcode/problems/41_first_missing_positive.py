from typing import List


"""
This is O(N) time and O(N) space

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        tmp = [0 for i in range(N)]
        for num in nums:
            if 0 < num <= N:
                tmp[num-1] += 1
        
        for idx, val in enumerate(tmp):
            if val == 0:
                return idx + 1
        return N + 1
"""

# This is O(N) time and O(1) space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        
        # move zeros and negatives to a number larger than N
        for idx, num in enumerate(nums):
            if num <= 0:
                nums[idx] = N + 1
        
        # mark an index as negative if it's positive
        for idx, num in enumerate(nums):
            abs_num = abs(num)
            if 0 < abs_num <= N:
                if nums[abs_num-1] > 0:
                    nums[abs_num-1] *= -1
        
        # result is the first index with positive value
        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
        
        # else, it's N+1
        return N + 1
