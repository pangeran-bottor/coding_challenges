from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums:
            if (abs(num) < abs(ans)) or (abs(num) == abs(ans) and num > ans):
                ans = num
        return ans
