from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        ans = float("-inf")
        for idx, num in enumerate(nums):
            left, right = idx + 1, n - 1
            while left < right:
                curr = num + nums[left] + nums[right]
                if abs(target - curr) <= abs(target - ans):
                    ans = curr
                if curr < target:
                    left += 1
                else:
                    right -= 1
        return ans
