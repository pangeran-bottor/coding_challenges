from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        farthest = 0
        end = 0

        N = len(nums)
        for i in range(N - 1):
            farthest = max(farthest, i + nums[i])

            if i + nums[i] >= N - 1:
                ans += 1
                break
            if i == end:
                ans += 1
                end = farthest
        return ans
