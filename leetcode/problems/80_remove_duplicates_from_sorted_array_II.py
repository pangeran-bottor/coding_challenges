from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0
        tmp = float("-inf")
        limit = 0
        
        for idx, num in enumerate(nums):
            if num != tmp:
                nums[result] = num
                result += 1
                limit = 1 
            else:
                if limit < 2:
                    nums[result] = num
                    result += 1
                limit += 1
            tmp = num
                
        return result
