from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ans = 1
        cur_max = nums[0]
        run_max = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] < cur_max:
                ans = i + 1
                cur_max = run_max
            else:
                run_max = max(run_max, nums[i])
        return ans
