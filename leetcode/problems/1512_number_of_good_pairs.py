from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 0
            num_counts[num] += 1
        ans = 0
        for num, count in num_counts.items():
            ans += count*(count-1)//2
        return ans
        