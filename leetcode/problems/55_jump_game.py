from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        nums[N-2] >= 1 -> True
        nums[N-3]  >= 2 or nums[N-2] >= curr_leftmost

        curr_leftmost is nums[curr_leftmost] that can reach last index
        """
        n = len(nums)
        curr_leftmost = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= curr_leftmost:
                curr_leftmost = i

        return curr_leftmost == 0
