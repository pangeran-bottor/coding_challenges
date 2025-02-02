from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        invalid_count = 0
        if nums[0] < nums[-1]:
            invalid_count += 1

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                invalid_count += 1

        return invalid_count <= 1
