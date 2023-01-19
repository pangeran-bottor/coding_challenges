import collections
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]

        prefix_sums = collections.defaultdict(int)
        for num in nums:
            num = num % k
            prefix_sums[num] += 1

        ans = 0
        for k, v in prefix_sums.items():
            if k == 0:
                ans += v
            ans += v * (v - 1) // 2
        return ans
