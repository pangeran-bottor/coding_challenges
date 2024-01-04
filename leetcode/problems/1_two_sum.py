from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rmap = {}
        for idx, num in enumerate(nums):
            r = target - num
            if r in rmap:
                return [rmap[r], idx]

            rmap[num] = idx
