from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = None
        for num in nums:
            if count == 0:
                ans = num
                count = 1
            elif num == ans:
                count += 1
            else:
                count -= 1
        return ans
