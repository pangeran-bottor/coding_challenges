from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)

        ans = 0
        for count in counts.values():
            if count == 1:
                return -1

            ans += count // 3 + (count % 3 != 0)
        return ans
