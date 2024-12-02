from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        nums_set = set(nums)

        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break

            total += nums[i]

        while total in nums_set:
            total += 1
        return total
