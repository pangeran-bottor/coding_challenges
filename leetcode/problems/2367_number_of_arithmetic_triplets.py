from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        nums_set = set()
        for num in nums:
            if (num - diff) in nums_set and (num - 2*diff) in nums_set:
                ans += 1
            nums_set.add(num)
        return ans
