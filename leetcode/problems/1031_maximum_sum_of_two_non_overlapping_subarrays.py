from typing import List


class Solution:
    def maxSumTwoNoOverlap(self,
                           nums: List[int],
                           firstLen: int,
                           secondLen: int) -> int:
        N = len(nums)
        for i in range(1, N):
            nums[i] += nums[i-1]

        ans = nums[firstLen + secondLen - 1]
        first_max = nums[firstLen - 1]
        second_max = nums[secondLen - 1]

        for i in range(firstLen + secondLen, N):
            first_max = max(
                first_max,
                nums[i - secondLen] - nums[i - firstLen - secondLen]
            )
            second_max = max(
                second_max,
                nums[i - firstLen] - nums[i - firstLen - secondLen]
            )
            ans = max(
                ans,
                first_max + nums[i] - nums[i - secondLen],
                second_max + nums[i] - nums[i - firstLen]
            )

        return ans
