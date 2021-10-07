from typing import DefaultDict, List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        num_counts = DefaultDict(int)
        for num in nums:
            ans += num_counts.get(num - k, 0)
            ans += num_counts.get(num + k, 0)
            num_counts[num] += 1
        return ans
