from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        for num in nums:
            if num == val:
                continue

            nums[current] = num
            current += 1
        return current
