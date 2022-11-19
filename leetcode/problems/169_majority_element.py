from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter()
        
        n = len(nums)
        result = nums[0]
        for num in nums:
            counts[num] += 1

            if counts[num] > n//2:
                result = num
                break
        
        return result
