from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for num in nums:
            if nums[k] == num:
                continue

            k += 1
            nums[k] = num
        return k + 1
