from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums_sum = sum(nums)

        cur_min = float("inf")
        cur_max = float("-inf")
        min_sum = float("inf")
        max_sum = float("-inf")
        for num in nums:
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)

        if min_sum == nums_sum:
            return max_sum

        return max(max_sum, nums_sum - min_sum)
