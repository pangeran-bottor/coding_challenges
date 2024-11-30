from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1

        for idx, num in enumerate(nums):
            if num > 0:
                ans.append(idx + 1)
        return ans
