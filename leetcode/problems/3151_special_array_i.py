from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        parity = nums[0] % 2
        for num in nums[1:]:
            if parity == num % 2:
                return False
            parity = (parity + 1) % 2
        return True
