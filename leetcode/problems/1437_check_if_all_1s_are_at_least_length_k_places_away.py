from math import inf
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -inf
        for idx, num in enumerate(nums):
            if num == 0:
                continue

            if idx - prev - 1 < k:
                return False

            prev = idx
        return True
