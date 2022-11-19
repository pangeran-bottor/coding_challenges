from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def range_to_str(start, end):
            if start == end:
                return str(start)
            return f"{start}->{end}"
        
        if len(nums) == 0:
            return [range_to_str(lower, upper)]
        
        ans = []

        N = len(nums)

        if lower < nums[0]:
            ans.append(range_to_str(lower, nums[0]-1))
        
        for i in range(N-1):
            cur = nums[i]
            nxt = nums[i+1]
            if nxt-cur > 1:
                ans.append(range_to_str(cur+1, nxt-1))

        if nums[-1] < upper:
            ans.append(range_to_str(nums[-1]+1, upper))

        return ans
