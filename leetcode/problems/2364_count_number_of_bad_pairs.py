from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff_map: dict[int, int] = {}

        ans = 0
        for i in range(n):
            diff = nums[i] - i
            curr_good = diff_map.get(diff, 0)
            ans += i - curr_good

            diff_map[diff] = curr_good + 1
        return ans
