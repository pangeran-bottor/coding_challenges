from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans = sum(nums[:k])
        cur_sum = sum(nums[:k])

        for i in range(k, n):
            cur_sum += nums[i] - nums[i - k]
            ans = max(ans, cur_sum)

        return ans / k
