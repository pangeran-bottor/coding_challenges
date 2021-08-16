from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            el = nums[nums[i]]
            ans.append(el)
        return ans
