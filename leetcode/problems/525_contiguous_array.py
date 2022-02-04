from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        count = 0
        memo = {0: -1}
        for idx, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
                
            if count in memo:
                result = max(result, idx-memo[count])
            else:
                memo[count] = idx
        return result
