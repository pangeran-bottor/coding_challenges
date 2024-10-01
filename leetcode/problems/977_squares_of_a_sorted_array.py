from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N

        left, right = 0, N - 1
        while N:
            if abs(nums[left]) < abs(nums[right]):
                val = nums[right]
                right -= 1
            else:
                val = nums[left]
                left += 1
            ans[N - 1] = val**2
            N -= 1
        return ans
