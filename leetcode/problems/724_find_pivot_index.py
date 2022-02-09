from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        nums_sum = 0
        pre_sum = [0]
        for num in nums:
            nums_sum += num
            pre_sum.append(num + pre_sum[-1])
        pre_sum.append(0)
        
        result = -1
        for i in range(1, N+1):
            if pre_sum[i-1] == (nums_sum-pre_sum[i]):
                return i - 1
        return result
