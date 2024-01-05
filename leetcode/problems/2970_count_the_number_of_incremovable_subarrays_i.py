from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                rest = nums[:i] + nums[j:]
                for k in range(1, len(rest)):
                    if rest[k - 1] >= rest[k]:
                        break
                else:
                    ans += 1
        return ans
