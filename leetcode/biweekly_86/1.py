from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        N = len(nums)
        sum_set = set()
        for i in range(1, N):
            cur_sum = nums[i] + nums[i-1]
            if cur_sum in sum_set:
                return True
            sum_set.add(cur_sum)
        return False
