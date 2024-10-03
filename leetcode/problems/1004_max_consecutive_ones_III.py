from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        zeros = 0
        start = 0

        for idx, num in enumerate(nums):
            if num == 0:
                zeros += 1

            while (start <= idx) and (zeros > k):
                if nums[start] == 0:
                    zeros -= 1
                start += 1

            ans = max(ans, idx - start + 1)

        return ans
